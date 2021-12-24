import os
import shutil
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("textfile_dir", help="move text files to new directory logs/junit_feedback")
    args = parser.parse_args()

    print("\n")
    print(f"Gathering Text Files: \n\t {args.textfile_dir}")
    print()
    path_to_new_destination = f"{args.textfile_dir}/logs/junit_feedback"
    print(f"Moving to: {path_to_new_destination}")

    try:
        os.mkdir(path_to_new_destination)
    except (FileExistsError):
        pass
    except Exception as e:
        raise e

    files = os.listdir(args.textfile_dir)
    for file in files:
        if ".txt" in file:
            print()
            print(f"{args.textfile_dir}/{file}")
            os.rename(f"{args.textfile_dir}/{file}", f"{path_to_new_destination}/{file}")
            