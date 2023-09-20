import streamlit as st
from io import StringIO
import re

st.set_page_config(
    page_title="Scanning for Substring using regular expression",
    page_icon="👋",
)
st.title("Scanning for Substring using regular expression")


def initLayout():
    FILE_TYPES = ["log","rtf", "java","sql"]
    substringCheck = "substring\([^,]*,'[^',\s]*'\)"
    substringCheck1 = "select substring\(\'.*\'\s+from\s+\'.*\'\)"
    substringCheck2 = 'select substring\(\'.*\'\s+from\s+\'\S*\\"*.*\\"*\S*\'\s+for\s+\'\S+\'\)'
    st.write(substringCheck)
    keyword_list=[]
    found = 0
    
    uploaded_files = st.file_uploader("Choose multiple files for scanning", type=FILE_TYPES,accept_multiple_files=True)
    with st.spinner('Scanning in progress'):
        for uploaded_file in uploaded_files:
            data_string = uploaded_file.readlines()
            file_name = uploaded_file.name
            offset = 1
            
            substring_reg = re.compile(substringCheck,re.IGNORECASE)
            substring_reg1 = re.compile(substringCheck1,re.IGNORECASE)
            substring_reg2 = re.compile(substringCheck2,re.IGNORECASE)

            

            for line in data_string:
                found_str = substring_reg.findall(str(line))
                if len(found_str) != 0:
                    st.text(file_name+":"+ " Line:"+str(offset) + ":" + str(found_str))
                    found +=1
                #found_str1 = substring_reg1.findall(str(line))
                #if len(found_str1) != 0:
                    #st.text(file_name+":"+ " Line:"+str(offset) + ":" + str(found_str1))
                    #found +=1

                #found_str2 = substring_reg2.findall(str(line))
                #if len(found_str2) != 0:
                    #st.text(file_name+":"+ " Line:"+str(offset) + ":" + str(found_str2))
                    #found +=1

                offset+=1
            
    if found == 0:
        st.write("substring expression not found")

	
def main():
		initLayout()
		
if __name__ == "__main__":
	main()
