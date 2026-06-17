# Work-time levers

How much work does a country need to do, and how can it **share** that work? This
panel is one accounting identity:

> `hours to do = workers × weekly hours × weeks/year`
> `workers = working-age population × (1 − n%)`

The **hours to do** come from EXIOBASE (production hours), and fall when you reduce
industries. The **working-age population** comes from UN demographic data and depends
on the age band you choose.

## The four knobs

- **Start age** / **Retirement age** — define who is of working age. A wider band =
  more potential workers.
- **n% (non-employment)** — the share of working-age people *not* in full-time work
  (unemployment + studies, care, disability…). Default 20%.
- **Weeks per year** — working weeks (lower it to model holidays/leave).

## Both directions

- **Forward**: set the knobs → read the weekly hours per worker.
- **Inverse**: set a *target* (e.g. 32 h/week) → the panel solves what it would take
  (a retirement age, or an n%). If a target can't be reached with these settings, it
  says **"not achievable"** rather than inventing a number.

Cut an industry and watch the hours freed appear — fewer hours each, or room to
retire earlier.
