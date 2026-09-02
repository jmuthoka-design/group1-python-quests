# group1-python-quests

Python fundamentals quests 

## About

This repository contains Python scripts for all 30 quests across all 6 levels of the "Learn Python by Coding" curriculum, from variables and printing through to functions and the final Grand Challenge projects.

## Group Members & Contributions

Each member owns 2 of the 6 levels:

| Member | Levels Owned | Quests |
|---|---|---|
| [Mary Njuguna] | Level 1 – Variables & Printing | 1, 2, 3, 4, 5 |
| | Level 2 – User Input & Basic Math | 6, 7, 8, 9, 10 |
| [Jemima Wavinya] | Level 3 – Conditional Statements | 11, 12, 13, 14, 15 |
| | Level 4 – Loops | 16, 17, 18, 19, 20 |
| [Florence Dushime] | Level 5 – Functions | 21, 22, 23, 24 |
| | Level 6 – The Grand Challenge | 25, 26, 27, 28, 29, 30 |



## Directory Structure

```
group1-python-quests/
├── quests/
│   ├── quest_01_first_spell.py
│   ├── quest_02_naming_ceremony.py
│   ├── quest_03_treasure_chest.py
│   ├── ... (all 30 scripts)
│   └── quest_30_reflective_scribe.py
└── README.md
```

## Quests Completed

All 30 quests across all 6 levels:

| Level | Theme | Quests |
|---|---|---|
| 1 | Variables & Printing | 1–5 |
| 2 | User Input & Basic Math | 6–10 |
| 3 | Conditional Statements | 11–15 |
| 4 | Loops | 16–20 |
| 5 | Functions | 21–24 |
| 6 | The Grand Challenge | 25–30 |

## How to Run

Each script can be run individually with Python 3:

```bash
python3 quests/quest_01_first_spell.py
```

Most scripts from Quest 6 onward prompt for input via the terminal run them interactively and type your answers when prompted. A few notes on specific scripts:
- **Quest 25** (Number Wizard) picks a genuinely random secret number each run — there's no fixed answer to guess.
- **Quest 26** (Simple Calculator) accepts `add`, `subtract`, `multiply`, or `divide` as the operation input.
- **Quest 28** (Adventure Begins) has two distinct endings depending on the choices you make.

## Contributing for group members

1. Clone the repo:
   ```bash
   git clone https://github.com/<owner-username>/group1-python-quests.git
   cd group1-python-quests
   ```
2. Before starting work, pulled the latest changes:
   ```bash
   git pull origin main
   ```
3. Add or edit only the scripts for your assigned level(s).
4. Stage, commit, and push your changes:
   ```bash
   git add quests/quest_XX_name.py
   git commit -m "Add Quest XX: short description"
   git pull origin main
   git push origin main
   ```

## Peer Review

This group reviewed two peer groups' submissions as required by Deliverable 

## Notes

- All 30 scripts were tested in Python 3.12 before submission every conditional branch and loop boundary was run and confirmed to produce the expected output.
- **Quest 30** (Reflective Scribe) adds explanatory comments to three earlier scripts: ` quest_21_reusable_incantation.py , ` quest_22_personalized_scroll.py`, and ` quest_24_master_spell.py`. Each comment explains what the codde does.
