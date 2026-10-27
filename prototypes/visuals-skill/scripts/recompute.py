"""PROTOTYPE. Recompute every number a chart or title will use, straight from the data file.

Stands in for the skill's scripts/recompute step: the model never types a plotted number
itself, it reads them from this script's output. Stdlib only, so it runs on Claude Free.

Usage: python recompute.py <bookings.csv> [out.json]
"""
import csv, json, sys

rows = list(csv.DictReader(open(sys.argv[1], newline="")))
for r in rows:
    for k in r:
        if k != "month":
            r[k] = int(r[k])

def rate(missed, booked):
    return round(100 * missed / booked, 1)

def half(rs, ch):
    return rate(sum(r[ch + "_missed"] for r in rs), sum(r[ch + "_booked"] for r in rs))

before, after = rows[:6], rows[6:]  # text reminders started 1 Jul, online bookings only
out = {
    "months": [r["month"] for r in rows],
    "online_rate": [rate(r["online_missed"], r["online_booked"]) for r in rows],
    "phone_rate": [rate(r["phone_missed"], r["phone_booked"]) for r in rows],
    "online_before": half(before, "online"), "online_after": half(after, "online"),
    "phone_before": half(before, "phone"), "phone_after": half(after, "phone"),
}
def overall(rs):
    m = sum(r["online_missed"] + r["phone_missed"] for r in rs)
    b = sum(r["online_booked"] + r["phone_booked"] for r in rs)
    return m, b
m_b, b_b = overall(before); m_a, b_a = overall(after)
out["overall_before"] = rate(m_b, b_b)
out["overall_after"] = rate(m_a, b_a)
phone_missed_after = sum(r["phone_missed"] for r in after)
out["phone_share_of_missed_after"] = rate(phone_missed_after, m_a)
out["phone_share_of_bookings_after"] = rate(sum(r["phone_booked"] for r in after), b_a)
out["missed_after_total"] = m_a
out["phone_missed_after"] = phone_missed_after
# What-if, labelled as such on any slide: phone bookings reach the online after-rate.
proj = sum(r["online_missed"] for r in after) + out["online_after"] / 100 * sum(r["phone_booked"] for r in after)
out["overall_if_phone_matched"] = rate(proj, b_a)
out["online_booked_total"] = sum(r["online_booked"] for r in rows)
out["phone_booked_total"] = sum(r["phone_booked"] for r in rows)
out["online_drop_pct"] = round(100 * (1 - out["online_after"] / out["online_before"]))
out["overall_drop_pct"] = round(100 * (1 - out["overall_after"] / out["overall_before"]))

text = json.dumps(out, indent=1)
print(text)
if len(sys.argv) > 2:
    open(sys.argv[2], "w").write(text)
