"""Ticket 03: agreement between the gold author and a second human reader, on the four
cases accidentally double-labelled under the single-pass protocol.

Readings are hand-coded from the eight worksheets in
tools/quality-reviewer/v2/eval-cases-real/labeling/ (gitignored, local only). Only ordinal
readiness codes and agreement flags are reproduced here, no client findings, so this script is
safe to commit. Full analysis: eval-cases-real/_INTER-RATER-RECOVERY.md (local only).

Run: python .scratch/deliverable-reviewer/ticket-03-irr.py
Exact Clopper-Pearson via inverse regularized incomplete beta, no scipy dependency.
"""
import itertools, math
from fractions import Fraction

# --- exact Clopper-Pearson via regularized incomplete beta (mpmath-free) ---
def betacf(a,b,x):
    MAXIT,EPS,FPMIN=300,3e-16,1e-300
    qab,qap,qam=a+b,a+1.0,a-1.0
    c=1.0; d=1.0-qab*x/qap
    if abs(d)<FPMIN: d=FPMIN
    d=1.0/d; h=d
    for m in range(1,MAXIT+1):
        m2=2*m
        aa=m*(b-m)*x/((qam+m2)*(a+m2))
        d=1.0+aa*d
        if abs(d)<FPMIN: d=FPMIN
        c=1.0+aa/c
        if abs(c)<FPMIN: c=FPMIN
        d=1.0/d; h*=d*c
        aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2))
        d=1.0+aa*d
        if abs(d)<FPMIN: d=FPMIN
        c=1.0+aa/c
        if abs(c)<FPMIN: c=FPMIN
        d=1.0/d; de=d*c; h*=de
        if abs(de-1.0)<EPS: break
    return h

def betai(a,b,x):
    if x<=0: return 0.0
    if x>=1: return 1.0
    bt=math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)+a*math.log(x)+b*math.log(1.0-x))
    if x<(a+1.0)/(a+b+2.0): return bt*betacf(a,b,x)/a
    return 1.0-bt*betacf(b,a,1.0-x)/b

def beta_quantile(p,a,b):
    lo,hi=0.0,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if betai(a,b,mid)<p: lo=mid
        else: hi=mid
    return (lo+hi)/2

def clopper_pearson(k,n,alpha=0.05):
    lo=0.0 if k==0 else beta_quantile(alpha/2,k,n-k+1)
    hi=1.0 if k==n else beta_quantile(1-alpha/2,k+1,n-k)
    return lo,hi

def kappa(pairs,weights=None):
    cats=sorted(set([a for a,b in pairs])|set([b for a,b in pairs]))
    n=len(pairs)
    if weights is None: w=lambda i,j: 1.0 if i==j else 0.0
    elif weights=='linear':
        m=max(cats)-min(cats)
        w=lambda i,j: 1.0-abs(i-j)/m if m else 1.0
    elif weights=='quadratic':
        m=max(cats)-min(cats)
        w=lambda i,j: 1.0-((i-j)/m)**2 if m else 1.0
    po=sum(w(a,b) for a,b in pairs)/n
    ma={c:sum(1 for a,b in pairs if a==c)/n for c in cats}
    mb={c:sum(1 for a,b in pairs if b==c)/n for c in cats}
    pe=sum(ma[i]*mb[j]*w(i,j) for i in cats for j in cats)
    return po,pe,(po-pe)/(1-pe) if pe<1 else float('nan')

CASES=['real-02','real-08','real-12','real-13']
# readiness coded R0=0 .. R3=3.  A = second reader (MF/GS), B = MS (the gold author)
A=[2,3,1,3]                      # MF R2, MF R3, GS R1, GS R3
B_charitable=[2,0,1,2]           # MS R1-R2 straddle resolved to R2 (what the gold did)
B_pessimistic=[1,0,1,2]          # MS straddle resolved to R1 (the other limb)

for name,B in [('charitable (real-02 MS = R2)',B_charitable),('pessimistic (real-02 MS = R1)',B_pessimistic)]:
    pairs=list(zip(A,B))
    k=sum(1 for a,b in pairs if a==b); n=len(pairs)
    lo,hi=clopper_pearson(k,n)
    po,pe,ku=kappa(pairs)
    _,_,kl=kappa(pairs,'linear')
    _,_,kq=kappa(pairs,'quadratic')
    mad=sum(abs(a-b) for a,b in pairs)/n
    print(f"\n### READINESS, {name}")
    print(f"  exact match      {k}/{n} = {k/n:.3f}   95% CP CI [{lo:.3f}, {hi:.3f}]")
    print(f"  mean abs gap     {mad:.2f} readiness levels   max gap {max(abs(a-b) for a,b in pairs)}")
    print(f"  kappa unweighted {ku:.3f}  (Po={po:.3f} Pe={pe:.3f})")
    print(f"  kappa linear-w   {kl:.3f}")
    print(f"  kappa quadratic  {kq:.3f}")
    # jackknife: leave one case out
    jk=[]
    for i in range(n):
        sub=[p for j,p in enumerate(pairs) if j!=i]
        _,_,kk=kappa(sub)
        jk.append((CASES[i],kk))
    print("  leave-one-out kappa: "+", ".join(f"drop {c} -> {v:.3f}" for c,v in jk))

# --- must-catch: does the second reader's must-catch name the same defect as the gold's? ---
print("\n### MUST-CATCH (same defect named)")
for label,hits in [('strict',[0,0,1,0]),('lenient (real-02 counted as same actionability defect, as _LABELING-RECORD already claims)',[1,0,1,0])]:
    k=sum(hits); n=len(hits); lo,hi=clopper_pearson(k,n)
    print(f"  {label}: {k}/{n} = {k/n:.3f}  95% CP CI [{lo:.3f}, {hi:.3f}]")

print("\n### RESTRAINT CALL (is this a 'nothing rises to must-catch' case?)")
hits=[1,0,1,0]  # agree, disagree, agree, disagree
k=sum(hits); n=len(hits); lo,hi=clopper_pearson(k,n)
print(f"  agreement: {k}/{n} = {k/n:.3f}  95% CP CI [{lo:.3f}, {hi:.3f}]")
print("  second reader called restraint on real-08 and real-13; gold called restraint on neither.")

print("\n### TOP-ISSUE SEVERITY")
hits=[1,0,1,0]
k=sum(hits); n=len(hits); lo,hi=clopper_pearson(k,n)
print(f"  agreement: {k}/{n} = {k/n:.3f}  95% CP CI [{lo:.3f}, {hi:.3f}]")

print("\n### DIRECTION (sign test, MS stricter = negative)")
diffs=[b-a for a,b in zip(A,B_charitable)]
nz=[d for d in diffs if d!=0]
neg=sum(1 for d in nz if d<0)
p=2*sum(math.comb(len(nz),i) for i in range(0,min(neg,len(nz)-neg)+1))/2**len(nz)
print(f"  diffs (MS - other) = {diffs}; {neg} of {len(nz)} non-ties have MS stricter; two-sided sign test p = {min(p,1.0):.3f}")

print(chr(10)+"### HOW MANY PAIRS WOULD LICENSE A CLAIM")
print("(Clopper-Pearson lower bound on raw agreement, at the observed rate shown)")
for n in [4,8,12,16,20,25,30,40]:
    row=f"{n:>4}"
    for rate in [0.75,0.80,0.90]:
        k=round(n*rate); lo,hi=clopper_pearson(k,n)
        row+=f"   {k}/{n} [{lo:.2f},{hi:.2f}]"
    print(row)
