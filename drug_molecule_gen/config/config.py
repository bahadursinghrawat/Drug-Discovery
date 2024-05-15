import pathlib
import os
import sys
sys.path.append("/")
import drug_molecule_gen


PACAKGE_ROOT =pathlib.Path(drug_molecule_gen.__file__).resolve().parent
DATAPATH=os.path.join(PACAKGE_ROOT,"dataset")
SAVED_MODEL_PATH =os.path.join(PACAKGE_ROOT,"trained_model")
MAX_INPUT_SEQUENCE_LEN =52
MAX_OUTPUT_SEQUENCE_LEN=52

TRAIN_FILE="train.csv"
TEST_FILE="test.csv"

BASE_VOCABULARY=['6','p','4','7','r','[','o','+','H','\\','s','#','C','<',
                    '/','%','N','0','=','.','c','3','5','S','l','1','B','I','\n','(','O',
                    '-',')',']','8','P','9','n','F','2']

INPUT_VOCABULARY=['','[UNK]','6','p','4','7','r','[','o','+','H','\\','s','#','C','<',
                    '/','%','N','0','=','.','c','3','5','S','l','1','B','I','\n','(','O',
                    '-',')',']','8','P','9','n','F','2']


OUTPUT_VOCABULARY=['','[UNK]','6','p','4','7','r','[','o','+','H','\\','s','#','C','<',
                    '/','%','N','0','=','.','c','3','5','S','l','1','B','I','\n','(','O',
                    '-',')',']','8','P','9','n','F','2']

# if "__name__" == "__main__":  


