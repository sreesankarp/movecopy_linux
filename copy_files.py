#copy_paste
import os

_destination_path = input('Enter destination path : ')
_source_path = input('Enter source path : ')
if _destination_path[-1]!="/":
    _destination_path+="/"
if _source_path[-1]!="/":
    _source_path+="/"
_mode = (input("Enter 'c' for copy 'm' to move : ")).lower()

_total_files = os.listdir(_source_path)
_total_len = int(len(_total_files))
_confirm_prompt = (input(f"Do you want to continue to {'COPY' if _mode=='c' else 'MOVE'} - {_total_len} files from {_source_path} to {_destination_path} (y/n) : ")).lower()

if _confirm_prompt=='y':
    _checkpoint = int(input(f"Enter checkpoint range to display progress for {_total_len} files : "))
    print("Process Started, Please wait!")
    for i,file in enumerate(_total_files):
        try:
            command = f'{"cp" if _mode == "c" else "mv"} {_source_path}{file} {_destination_path}'
            os.system(command)
            if i%_checkpoint==0:
                print("Progress : ",int(i/_total_len),"%")
        except Exception as x:
            print(" --> Error : ",x)
