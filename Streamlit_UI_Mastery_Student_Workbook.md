# Streamlit UI Mastery: Building the Dashboard (Module 3) - Student Workbook
*Turning Data Logic into a Modern Web Application*

**Instructions:** This is your Week 3 workbook. Follow each section and fill in the placeholder code blocks during class or practice.

**Goal:** By the end of this module, students will have a running web app that can Create, Read, Update, and Delete assignments using a graphical interface instead of the terminal.

## Week Plan
**Monday:** Segments 0-4 (Setup through Text Elements)
**Wednesday:** Segments 5-19 (Inputs through File Persistence)

---

## Agenda
1. Project & Repo Setup (The Foundation)
2. Installation & Environment (The Tools)
3. Create `app.py`
4. Running the Streamlit App
5. The Hierarchy of Information (Text Elements)
6. Data Entry (The Input Layer)
7. Buttons & Action Triggers (`st.button`)
8. Markdown & Text Formatting (`st.markdown`)
9. Selection Widgets (Choosing Options)
10. Feedback & Status (UX)
11. Layout Containers - Organizing the Screen: Columns
12. Layout Containers - Organizing the Screen: Tabs (`st.tabs`): Clicking to Switch Views
13. Item Keys (`key`)
14. `st.session_state` (Remember Navigation State)
15. `st.rerun()` (Immediate Refresh)
16. Interaction & Navigation (The Flow)
17. Full Integrated Example (No State/Rerun)
18. Local File Persistence (`json`)
19. Data & Performance (The Engineering)
20. The Mental Model (Crucial Concept)

---

## Continuity From Week 2
- Week 2 built the **data engine** for the Assignment Manager using lists, dictionaries, loops, and CRUD patterns by `id`.
- Week 3 builds the **UI layer** for that same project using Streamlit.
- In `Project_Evolution_Spec.md`, this is still **Phase 1** ("Spaghetti Prototype"): single-script flow with in-memory data, now with a web interface.

---

## 0. Project & Repo Setup (The Foundation)
**Goal:** Create the project repo manually, build the local folder, and connect both.

### Step A: Create the GitHub Repository (Manual)
1.  Go to GitHub and click **New repository**.
2.  Set the repository name to `assignment-manager-streamlit`.
3.  Choose visibility (Public or Private) based on course instructions.
4.  Create the repo and copy its HTTPS URL (example: `https://github.com/YOUR_USERNAME/assignment-manager-streamlit.git`).

### Step B: Create the Local Project Folder
1.  Create a local folder named `assignment-manager-streamlit`.
2.  Open that folder in VS Code.
3.  Keep all course project files in this one root folder.
4.  Add Week 3 files directly in the root (no subfolder).

### Step C: Initialize Git and Connect to GitHub
Run these commands in the VS Code terminal from the project root:

```bash
git init
git branch -M main
git remote add origin https://github.com/asilicato/assignment-manager-streamlit.git
git remote -v
```

If you already have an `origin`, update it instead:

```bash
git remote set-url origin https://github.com/asilicato/assignment-manager-streamlit.git
git remote -v
```

Then make your first push:

```bash
git add .
git commit -m "Initial Week 2 + Week 3 project setup"
git push -u origin main
```

Also confirm:
1.  `.gitignore` includes Python + secret files (`.env`, `.venv/`, `__pycache__/`, `*.pyc`).
2.  `.env` exists at the project root.

---

## 1. Installation & Environment (The Tools)
**Goal:** Install Streamlit and understand common setup errors.

### Step A: The Install Command
Run this in your terminal to install the library:
```bash
python3 -m pip install streamlit
# Windows users might use: py -m pip install streamlit
```

### Step B: Common Installation Errors (Troubleshooting)

| Error Message | What it Means | How to Fix |
| :--- | :--- | :--- |
| **`command not found: pip`** | Your terminal doesn't know where `pip` is. | Use `python3 -m pip` instead of just `pip`. |
| **`No module named streamlit`** | You installed it, but Python can't find it. | You might have multiple Pythons. Ensure you use the same command (`python3`) for installing and running. |
| **`Permission denied`** | You don't have admin rights. | Add `--user` to the command: `pip install --user streamlit`. |
| **`Connection timeout`** | Internet blocked the download. | Try a different wifi or VPN. |

### Step C: Add a `requirements.txt` File
Add a dependency file so anyone can install the same libraries for this project.

1. Create `requirements.txt` in the project root.
2. Add this line to the file:
   ```txt
   streamlit
   ```
3. Install from the file:
   ```bash
   python3 -m pip install -r requirements.txt
   # Windows users might use: py -m pip install -r requirements.txt
   ```

---

## 2. Create app.py
**Goal:** Create the starter Streamlit file.

### Step A: Create the File
1.  Create a new file named `app.py` in the project root.
    *   *Project rule:* Keep this Week 3 file in the root (no subfolder).
2.  Add this code:
    ```python
    import streamlit as st

    st.title("AI Course Manager")
    st.write("Week 3 UI layer connected to the Week 2 Assignment Manager data model.")
    st.button("Click me")
    ```

---

## 3. Running the Streamlit App
**Goal:** Start the local Streamlit server and understand the rerun workflow.

### Step A: The "Run" Command
To see your app, you don't use the "Play" button in VS Code. You must run a **Streamlit server**.
```bash
# TODO: Add the command to run Streamlit for app.py from the project root.
```

*   **Action:** A browser window should pop up (usually at `http://localhost:8501`).
*   **The Golden Rule:** whenever you change code, **Ctrl+S (Save)** the file, then click **"Rerun"** in the browser.


---

## 4. The Hierarchy of Information (Text Elements)
*From "Script" to "Application UI".*

In the "Course Manager" running case, we need an interface that looks organized, not just a list of print statements.

**Reference:** `Streamlit_UI_Curriculum.md` > Section 1 (Structure) & 5 (Formatting)

### A. The Hierarchy of Main Elements
Before we arrange things, we must label them clearly. Streamlit uses a hierarchy of headings to help users understand page structure.

*   **`st.title` (The Brand):** The main name of the application (e.g., "Assignments Dashboard").
*   **`st.header` (The Section):** Major divisions (e.g., "Current Term", "Archives").
*   **`st.subheader` (The Card):** Specific item labels (e.g., "Homework 1 Details").
*   **`st.caption` (The Instruction):** Small text for context (e.g., "All times are EST").

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

---

## 5. Data Entry (The Input Layer)
*Capturing user data.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 2

Streamlit provides widgets for every data type.

| Data Type | Widget |
| :--- | :--- |
| Text | `st.text_input("Label")` |
| Paragraph | `st.text_area("Label")` |
| Number | `st.number_input("Label", min_value=0)` |
| Date | `st.date_input("Due Date")` |

### Coding an "Assignment Draft" Input Panel
Inside your app, add this:

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

> **Teacher Note:** This example is intentionally "live update." As students type, Streamlit reruns and refreshes the preview.


---

## 6. Buttons & Action Triggers (`st.button`)
*Running logic only when the user clicks.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 2 and Section 4

### Why `st.button` Matters
Unlike text inputs (which rerun on every change), a button is a clear **action signal**.  
Use buttons for submit, save, reset, delete, and navigation triggers.

### Pattern: Define Button, Then Check Click State
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Use 1: Basic Click Action
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Use 2: Click + Validation
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Use 3: Multiple Buttons Need Unique Keys
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


---

## 7. Markdown & Text Formatting (`st.markdown`)
*Presenting information clearly with styled text.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 5

### Use 1: Emphasis and Structure
Use markdown to create readable sections, emphasis, and lists.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Use 2: Color-Coded Status Signals
Use Streamlit color tokens inside markdown to make status easier to scan.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Use 3: Dynamic Messages with Variables
Combine markdown with f-strings to show live values from inputs.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Use 4: Links and Notes
Use markdown for quick links and inline guidance.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


---

## 8. Selection Widgets (Choosing Options)
*Selecting from predefined options.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 2

When users should pick from known choices, use selection widgets instead of free typing.

### `st.radio` (Pick One)
**Purpose:** Make the user choose exactly one option from a short visible list.  
**Use when:** Options are mutually exclusive and you want quick comparison.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.checkbox` (Yes/No)
**Purpose:** Capture a boolean choice (`True` or `False`).  
**Use when:** The setting is optional and independent.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.selectbox` (One Choice from Many)
**Purpose:** Let users pick exactly one option from a dropdown list.  
**Use when:** You have many options and want to save vertical space.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.multiselect` (Choose Multiple)
**Purpose:** Let users choose zero, one, or many options from a list.  
**Use when:** Users need to filter or tag items by multiple categories at once.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Additional Selector
| Widget | Purpose | Best Use Case |
| :--- | :--- | :--- |
| `st.select_slider` | Pick one option along an ordered scale | Ordered values such as priority (`Low`, `Medium`, `High`) |


---

## 9. Feedback & Status (UX)
*Talking back to the user with clear UI signals.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 3

### `st.success` (Green)
**Purpose:** Confirm a completed action.  
**Use when:** An operation finishes correctly.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.error` (Red)
**Purpose:** Show blocking problems that must be fixed.  
**Use when:** Validation fails.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.warning` (Yellow)
**Purpose:** Highlight caution before a risky action.  
**Use when:** The user can proceed but should review first.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.info` (Blue)
**Purpose:** Give neutral context and guidance.  
**Use when:** You want to explain app state.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.spinner` and `st.progress` (Processing Feedback)
**Purpose:** Show that a long task is running.  
**Use when:** Loading, generating, or syncing data.

> **Syntax Note (`with`):** In Streamlit, `with` opens a UI context (such as a sidebar, column, expander, or spinner). Every indented line under it is rendered inside that context.
>
> Common usage patterns:
> - `with st.sidebar:`
> - `with st.container(border=True):`
> - `with col1:`
> - `with tab_edit:`
> - `with st.expander("Advanced Configuration"):`
> - `with st.spinner("Saving..."):`

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.metric` (Dashboard Snapshot)
**Purpose:** Show key numbers at a glance.  
**Use when:** Building a dashboard header.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


**Git Checkpoint:**
- Commit message: `Week 3 - Inputs and Feedback`

---

## 10. Layout Containers - Organizing the Screen: Columns
A professional app isn't just one long column. We group related information.

**1. Container (`st.container`): Grouped Content Block**
*   **Use Case:** Wrapping related elements into one visual unit.
*   **Context:** Group assignment summary details before showing editing controls.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

**2. Expander (`st.expander`): Collapsible Advanced Details**
*   **Use Case:** Hiding optional or advanced settings to keep the main screen clean.
*   **Context:** Keep rubric options or extra configuration available but out of the way.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

**3. Columns (`st.columns`): Side-by-Side Content**
*   **Use Case:** Dashboard metrics or splitting Menu vs Content.
*   **Context:** Put the "Navigation Menu" on the left (1/3 width) and "Assignment Details" on the right (2/3 width).

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Example 2: Columns Inside Columns (Nested Layout)
Use nested columns when one main area needs smaller sub-panels (for example, KPI cards above a table).

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

---

## 11. Layout Containers - Organizing the Screen: Tabs (st.tabs): Clicking to Switch Views
*   **Use Case:** Avoiding "Endless Scrolling".
*   **Context:** An instructor needs to *Edit* an assignment, then immediately *Preview* what a student sees.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

---

## 12. Item Keys (`key`)
*Giving each widget a unique identity when needed.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 4

### Why Keys Matter
Streamlit tracks widgets by their type and label.  
If two widgets look identical, Streamlit can get confused unless you assign different keys.

### Example: Duplicate Labels Require Keys
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### Example: Keys Inside Repeated UI (Loops)
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


---

## 13. `st.session_state` (Remember Navigation State)
*Persisting values across reruns.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 4

### Why `st.session_state` Matters
Regular Python variables reset every rerun.  
Use `st.session_state` when a value (such as active page or selected item) should survive across interactions.

### Basic Example
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


---

## 14. `st.rerun()` (Immediate Refresh)
*Forcing instant screen refresh after state changes.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 4

### Why `st.rerun()` Matters
When your code updates state (for example, changing pages), you may want the UI to refresh immediately so the new view appears without waiting for another interaction.

### Basic Example
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### How `key` and `st.rerun()` Work Together
If multiple action buttons can trigger rerun, give each button a unique key to avoid collisions.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


---

## 15. Interaction & Navigation (The Flow)
*Making it feel like an App, not a Script.*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 4

### Example: Navigation Without Sidebar
```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


---

## 16. Full Integrated Example (No State/Rerun)
*Putting covered concepts together in one script without using `st.session_state` or `st.rerun()`.*

**Goal:** Build a mini "AI Course Manager" screen using only covered UI pieces and an in-memory list of dictionaries.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


---

## 17. Local File Persistence (`json`)
*Reading and recording assignment data in a local JSON file.*

**Goal:** Save records to disk so they are still available after app reruns/restarts.

### Why This Matters
- Week 2 and most Week 3 demos used in-memory lists.
- This section adds simple persistence using a local JSON file in the project root.
- CSV is moved to **Appendix A** (optional).

### Step A: Create Starter JSON File in Project Root
Create `assignments.json` with this starter content.
If your instructor shares `files/week3_assignments_starter.json`, copy that content into your project root `assignments.json`.
```json
[
  {
    "id": "HW1",
    "title": "ER Model",
    "description": "Submit ER diagram with entities and relationships.",
    "point": 100
  },
  {
    "id": "LAB1",
    "title": "SQL Practice",
    "description": "Write basic SELECT queries with WHERE filters.",
    "point": 20
  }
]
```

### Step B: Read Records From `assignments.json`
Use Python `json` plus `Path` from `pathlib`.

```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Define JSON_PATH in the project root.
# 2) Create json_records = [].
# 3) If JSON_PATH exists, open and load with json.load().
# 4) Display the loaded list.
```

### Step B.1: Apply JSON Column Conversions (Optional)
```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Loop through each row in json_records.
# 2) Strip spaces for id/title/description.
# 3) Convert point to int when possible; otherwise set point to 0.
# 4) Use row.get("title", "") style access to avoid errors if a key is missing.
# 5) Use .strip() to remove extra spaces at the start/end of text.
```

### Step C: Collect New Input For `assignments.json`
```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Collect id/title/description/point using Streamlit inputs.
# 2) Use unique keys for widgets.
```

### Step D: Save a New Record To `assignments.json`
```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Use st.button("Save to JSON") to trigger save.
# 2) Validate id/title are not empty.
# 3) Append the new record to json_records.
# 4) Write the list with json.dump(..., indent=2).
```

### Step D.1: Debug JSON Data with `st.json`
```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Build a debug_payload dictionary (file_path, record_count, latest_record).
# 2) Display it with st.json(debug_payload).
```

### Step E: Verify Persistence
1. Run the app, save 2-3 records.
2. Stop Streamlit, run it again.
3. Confirm your saved records still load from file.

---

## 18. Data & Performance (The Engineering)
*Crucial for Phase 3 (OOP) and Phase 4 (Services).*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 6

### `st.dataframe` vs `st.table`
**Usage:** Displaying the "List of All Assignments". `dataframe` is interactive (sortable), `table` is static.
**List-of-dicts note:** No pandas needed for this section. Use a list of dictionaries directly with `st.dataframe`.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.cache_data`
**Usage:** Wrapping the "Database Fetch" function so we don't reload data on every rerun.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

### `st.file_uploader` (Attach Files)
**Usage:** Attaching PDF resources or reference images to an assignment.

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```


**Git Checkpoint:**
- `git add .`
- `git commit -m "Week 3 - Completed Dashboard UI"`
- `git push`

---

## 19. The Mental Model (Crucial Concept)
*Understanding how Streamlit "thinks".*

**Reference:** `Streamlit_UI_Curriculum.md` > Section 0

### The Rerun Cycle
**Core idea:** Every interaction reruns the script from top to bottom.

### Volatile Variables vs. Persistent State
**Core idea:** Regular variables reset on rerun; `st.session_state` remembers values across reruns.

### Control Flow Drives the UI
**Core idea:** The current state determines what the user sees (`if/elif` branches).

```python
# TODO: Write your Python/Streamlit code for this section.
# TODO: Use the instructions above to complete this block.
```

---

## Appendix A. CSV Version (Optional)
*Use this if you want the same workflow with CSV.*

### Step A1: Create `assignments.csv` in the project root
```csv
id,title,description,point
```

### Step A2: Read Records From `assignments.csv`
```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Define CSV_PATH in the project root.
# 2) Create csv_records = [].
# 3) If CSV_PATH exists, open with csv.DictReader and append rows.
# 4) Display the loaded rows.
```

### Step A2.1: Apply CSV Column Conversions (Optional)
```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Loop through each row in csv_records.
# 2) Strip spaces for id/title/description.
# 3) Convert point to int when possible; otherwise set point to 0.
```

### Step A3: Collect New Input For `assignments.csv`
```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Collect id/title/description/point using Streamlit inputs.
# 2) Use keys different from JSON keys.
```

### Step A4: Save a New Record To `assignments.csv`
```python
# TODO: Write your Python/Streamlit code for this section.
# Hints:
# 1) Use st.button("Save to CSV") to trigger save.
# 2) Validate id/title are not empty.
# 3) Append the new record to csv_records.
# 4) Write rows using csv.DictWriter with fieldnames = ["id", "title", "description", "point"].
```
