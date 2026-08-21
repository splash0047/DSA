import os, glob, re

# Read all problem folders and their question files in the repo
repo_folders = glob.glob(r'c:\Users\Pinak chimurkar\DSA\Phase *\*')
repo_folders = [f for f in repo_folders if os.path.isdir(f)]

repo_problems_by_lc = {}
repo_problems_by_title = {}

for f in repo_folders:
    folder_name = os.path.basename(f)
    phase_name = os.path.basename(os.path.dirname(f))
    num = folder_name[:3]
    title = folder_name[4:].strip().lower()
    
    # Read 00_Question.md to find LeetCode #
    q_file = os.path.join(f, '00_Question.md')
    lc_num = None
    if os.path.exists(q_file):
        with open(q_file, 'r', encoding='utf-8', errors='ignore') as qf:
            content = qf.read()
            match = re.search(r'LeetCode\s*#?(\d+)', content, re.IGNORECASE)
            if match:
                lc_num = int(match.group(1))
    
    clean_title = re.sub(r'[^a-z0-9]', '', title)
    repo_problems_by_title[clean_title] = {
        'folder': folder_name,
        'phase': phase_name,
        'path': f,
        'lc': lc_num
    }
    if lc_num:
        repo_problems_by_lc[lc_num] = {
            'folder': folder_name,
            'phase': phase_name,
            'path': f,
            'title': folder_name[4:]
        }

from compare_pdf_vs_repo import pdf_problems

solved = []
missing = []

for no, title, lc_str, phase in pdf_problems:
    lc_match = re.search(r'#(\d+)', lc_str)
    lc_id = int(lc_match.group(1)) if lc_match else None
    
    clean_title = re.sub(r'[^a-z0-9]', '', title.lower())
    
    matched = None
    if lc_id and lc_id in repo_problems_by_lc:
        matched = repo_problems_by_lc[lc_id]
    elif clean_title in repo_problems_by_title:
        matched = repo_problems_by_title[clean_title]
    
    if matched:
        solved.append((no, title, lc_str, phase, matched))
    else:
        missing.append((no, title, lc_str, phase))

print(f"=== SUMMARY ===")
print(f"Total PDF Questions: {len(pdf_problems)}")
print(f"Solved / Present in Repo: {len(solved)}")
print(f"Missing from Repo: {len(missing)}")

print("\n=== MISSING QUESTIONS FROM PDF ===")
for m in missing:
    print(f"[{m[3]}] #{m[0]:03d} - {m[1]} ({m[2]})")

print("\n=== EXTRA QUESTIONS IN REPO (NOT IN THIS PDF LIST) ===")
pdf_lc_set = {int(re.search(r'#(\d+)', lc).group(1)) for _, _, lc, _ in pdf_problems if re.search(r'#(\d+)', lc)}
pdf_title_set = {re.sub(r'[^a-z0-9]', '', t.lower()) for _, t, _, _ in pdf_problems}

for f in repo_folders:
    name = os.path.basename(f)
    t_clean = re.sub(r'[^a-z0-9]', '', name[4:].lower())
    # check if in pdf
    found = False
    if t_clean in pdf_title_set:
        found = True
    else:
        # check lc
        q_file = os.path.join(f, '00_Question.md')
        if os.path.exists(q_file):
            with open(q_file, 'r', encoding='utf-8', errors='ignore') as qf:
                c = qf.read()
                m = re.search(r'LeetCode\s*#?(\d+)', c, re.IGNORECASE)
                if m and int(m.group(1)) in pdf_lc_set:
                    found = True
    if not found:
        print(f"Extra in Repo: [{os.path.basename(os.path.dirname(f))}] {name}")
