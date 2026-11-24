import sys

THRESHOLD = 3 


def load_entries(filename):
    entries = []
    skipped = 0
    with open(filename) as  log_file:
        for line in log_file:
            parts = line.split() 
            if len(parts) == 4 and parts[3] in ("SUCCESS", "FAILED"):
                entries.append((parts[2], parts[3])) 
            else:
                skipped    += 1 
    return entries, skipped

def count_failures(entries):
    counts = {}
    for username, status in entries:
        if status == "FAILED":
            counts[username] = counts.get(username, 0) + 1
    return counts


def find_flagged_users(counts, threshold=THRESHOLD):
    return sorted(user for user, n in counts.items() if n >= threshold)


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "auth.log"
    try:
        entries, skipped = load_entries(filename)
    except FileNotFoundError:
        print(f"Error: log file '{filename}' was not found.")
        return
    counts = count_failures(entries)
    print(f"Entries analyzed: {len(entries)} (skipped {skipped} bad lines)")
    print(f"Total failed attempts: {sum(counts.values())}")
    print("Failures per user:")
    for user, n in sorted(counts.items()):
        print(f"  {user}: {n}")
    print(f"Flagged users (>= {THRESHOLD} failures): {find_flagged_users(counts)}")


if __name__ == "__main__":
    main()
