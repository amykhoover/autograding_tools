import os
import argparse
import zipfile

if __name__ =="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("unzip_dir", help="unzip the files in this directory")
    args = parser.parse_args()

    print("\n")
    print(f"Unzipping files in folder (args.unzip_dir): \n\t {args.unzip_dir}")

    directories = os.listdir(args.unzip_dir)

    extractedDir = f"{args.unzip_dir}/extracted"
    print(f"Making folder for extracted zip files (extractedDir): \n\t {extractedDir}")
    try:
        os.mkdir(extractedDir)
    except (FileExistsError):
        pass
    except Exception as e:
        raise e

  
    for item in directories:
        if ".DS_Store" not in item:
            print("\n")
            
            path_to_zip_file = f"{args.unzip_dir}/{item}"
            print(f"Path to zip file (item):{path_to_zip_file}")
            directory_to_extract_to = f"{extractedDir}/{item}"
         
            try:
                os.mkdir(directory_to_extract_to)
            except (FileExistsError):
                pass
            except Exception as e:
                raise e

            with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to)
