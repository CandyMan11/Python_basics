import json

#function to get filename
def get_filename(file_name, extension=".txt"):
    if file_name.endswith(".txt") or file_name.endswith(".json"):
        return file_name
    else:
        return file_name + extension

#fucntion to display questions one-by-one
def run_quiz(questions):
    score = 0

    for i, q in enumerate(questions, start=1):
        ans = input(f"Q{i}. {q['q']} ")

        if ans.strip().lower() == q["a"].strip().lower():
            score += 1

        else:
            continue

    print(f"\nYour score: {score}/{len(questions)}")

def main():
    file = get_filename("ques.json")

    try:
        with open(file, "r") as file:
            questions = json.load(file)
        run_quiz(questions)

    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")

    except json.JSONDecodeError:
        print(f"Error: File '{file}' is not a valid JSON file.")

if __name__ == "__main__":
    main()