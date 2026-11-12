from pathlib import Path
from collections import Counter
OUTPUT_TXT=Path("word_counts.txt")
OUTPUT_CSV=Path("word_counts.csv")
counts=Counter({"python": 5, "code": 3, "file": 2})
def write_summary_txt(counter,path:Path):
    lines=["Word Frequeency Summary\n","=======================\n"]
    for word,freq in counter.most_common():
        lines.append(f"{word:20s}{freq}\n")
    with path.open("w",encoding="utf-8") as f:
        f.writelines(lines)

def write_summary_csv(counter, path:Path):
    import csv
    with path.open("w",newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word","count"])
        for word, freq in counter.most_common():
            writer.writerow([word, freq])
write_summary_txt(counts,OUTPUT_TXT)
write_summary_csv(counts,OUTPUT_CSV)
