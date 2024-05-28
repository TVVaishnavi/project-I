 
import pandas as pd
import fitz



id=[]
domain=[]
s_skill=[]
difficulty=[]
correct_ans=[]
ans_reason=[]
chose_a=[]
chose_b=[]
chose_c=[]
chose_d=[]
main_Question=[]
prompt=[]
i=1
while i<910:
    pdf=i
    doc=fitz.open("1 ({}).pdf".format(pdf))
    text=""
    for page in doc:
       text+=page.get_text()

    Taking_Question=text.split("\n")      
    Taking_table=text.split()           

    Pdf_len_Q=len(Taking_Question)
    Pdf_len_T=len(Taking_table)
    For_chose=len(Taking_Question)
       

    def find_Index_For_Question(name):  
          i=0
          while i<=Pdf_len_Q:
                if Taking_Question[i]==name:
                   return i
                i+=1


    def find_Index_for_Elements_And_Table(name): 
          i=0
          while i<=Pdf_len_T:
                if Taking_table[i]==name:
                   return i
                i+=1

    def Cut_THe_Paragraph(start,end):    
          paragraph=[]
          y=end-6
          x=start+1
          while x<y:
            paragraph.append(Taking_Question[x])
            x+=1
          return paragraph


    def Cut_THe_Paragraph_correct(start,end):   
          paragraph=""
          y=end-1
          x=start+3
          while x<y:
            paragraph+=Taking_Question[x]
            x+=1
          return paragraph

   
    deff="Diﬃculty"
    delf="Question"
    Qdf="Assessment"
    Domain="Domain"
    skill="Skill"
    ID="ID"
    Sid="ID:"
    A="A."
    B="B."
    C="C."
    D="D."
    Correct="Answer:"
    
    def cut_chose(start,end):
          paragraph=""
          y=end
          x=start+1
          while x<y:
            paragraph+=" "+Taking_table[x]
            x+=1
          return paragraph

    def find_Index_chose(name): 
          i=0
          while i<=Pdf_len_T:
                if Taking_table[i]==name:
                   if find_Index_for_Elements_And_Table(D)<i:
                      return i
                i+=1
    
    lest=[]
    z=0
    while z<For_chose:
          for letter in Taking_Question[z]:
              lest.append(letter)
          z+=1
    
    def find_Index_for_lest(name): 
          i=0
          while i<=len(lest):
                if lest[i]==name:
                   return i
                i+=1
      
    def find_Index_for_lest_cho(start,name): 
          i=start
          while i<=len(lest):
                if lest[i]==name:
                   return i
                i+=1
    
    def cut_chose_word(start,end):
          word=""
          y=end
          x=start
          while x<y:
            word+=lest[x]
            x+=1
          return word
    
    I_Correct_k=Taking_table[find_Index_for_Elements_And_Table(Correct)+1]   
    if(i==909):
         I_A_k=cut_chose_word(find_Index_for_lest_cho(find_Index_for_lest("?"),"A"),find_Index_for_lest_cho(find_Index_for_lest("?"),"s"))
         I_B_k=cut_chose_word(find_Index_for_lest_cho(find_Index_for_lest("?"),"s"),find_Index_for_lest_cho(find_Index_for_lest("?"),"C"))
    else:
         I_A_k=cut_chose_word(find_Index_for_lest_cho(find_Index_for_lest("?"),"A"),find_Index_for_lest_cho(find_Index_for_lest("?"),"B"))
         I_B_k=cut_chose_word(find_Index_for_lest_cho(find_Index_for_lest("?"),"B"),find_Index_for_lest_cho(find_Index_for_lest("?"),"C"))

         
    I_C_k=cut_chose_word(find_Index_for_lest_cho(find_Index_for_lest("?"),"C"),find_Index_for_lest_cho(find_Index_for_lest("?"),"D"))
    I_D_k=cut_chose_word(find_Index_for_lest_cho(find_Index_for_lest("?"),"D"),find_Index_for_lest_cho(find_Index_for_lest("?"),"I"))
    I_ID_K=Taking_table[find_Index_for_Elements_And_Table(ID)+1]
    I_Deff_K=Taking_table[find_Index_for_Elements_And_Table(Qdf)-1]
    I_Domain_k=cut_chose(find_Index_for_Elements_And_Table(Domain),find_Index_for_Elements_And_Table(skill))
    I_Skill_K=cut_chose(find_Index_for_Elements_And_Table(skill),find_Index_for_Elements_And_Table(deff))
    para_start="Question ID {}".format(I_ID_K)
    I_correct_ans_k=Cut_THe_Paragraph_correct(find_Index_For_Question(para_start),find_Index_For_Question(Qdf))
    
    IDQ="Diﬃculty"
   
    
    id.append(I_ID_K)
    domain.append(I_Domain_k)
    s_skill.append(I_Skill_K)
    Q_Qdf.append(I_Deff_K)
    correct_ans.append(I_Correct_k)
    ans_reason.append(I_correct_ans_k)
    chose_a.append(I_A_k)
    chose_b.append(I_B_k)
    chose_c.append(I_C_k)
    chose_d.append(I_D_k)
    print(i)
    
    Question=Cut_THe_Paragraph(find_Index_For_Question(IDQ)+2,Pdf_len_Q)
    Question_len=len(Question)


    lest_q=[]
    z=0
    while z<Question_len:
          for letter in Question[z]:
              lest_q.append(letter)
          z+=1
    
   
    
    def find_Index_for_lest_Question(name): 
              i=0
              while i<=len(lest_q):
                    if lest_q[i]==name:
                       return i
                    i+=1
    

    lest_q_c=[]
    z=0
    while z<=find_Index_for_lest_Question("?"):
          for letter in lest_q[z]:
              lest_q_c.append(letter)
          z+=1
      
    
    def find_Index_for_lest_Question_sl(name): 
              i=-1
              while i<=-1:
                    if lest_q_c[i]==name:
                       return i
                    i-=1

    def cut_para_Q(start,end):
          para="" 
          i=start
          while i<=end:
                para+=" "+Taking_table[i]
                i+=1
          return para
    
    if(I_ID_K=="14b7dced"):
       I_sample_question=cut_para_Q(find_Index_for_Elements_And_Table("Which"),find_Index_for_Elements_And_Table("text?"))
       I_main_question=cut_para_Q(find_Index_for_Elements_And_Table("The"),find_Index_for_Elements_And_Table("Which")-1)
    elif(I_ID_K=="59e41600"):
       I_sample_question=cut_para_Q(find_Index_for_Elements_And_Table("Which"),find_Index_for_Elements_And_Table("English?"))
       I_main_question=cut_para_Q(find_Index_for_Elements_And_Table("Why"),find_Index_for_Elements_And_Table("Which")-1)
    elif(I_ID_K=="81ac953e"):
       I_sample_question=cut_para_Q(find_Index_for_Elements_And_Table("Which"),find_Index_for_Elements_And_Table("English?"))
       I_main_question=cut_para_Q(find_Index_for_Elements_And_Table("In"),find_Index_for_Elements_And_Table("Which")-1)
    elif(I_ID_K=="c101fc44"):
       I_sample_question=cut_para_Q(find_Index_for_Elements_And_Table("Which"),find_Index_for_Elements_And_Table("English?"))
       I_main_question=cut_para_Q(find_Index_for_Elements_And_Table("How"),find_Index_for_Elements_And_Table("Which")-1)
    elif(I_ID_K=="d72b325e"):
       I_sample_question=cut_para_Q(find_Index_for_Elements_And_Table("Based"),find_Index_for_Elements_And_Table("1?"))
       I_main_question=cut_para_Q(find_Index_for_Elements_And_Table("Text"),find_Index_for_Elements_And_Table("Based")-1)
    else:               
       I_sample_question=""
       z=len(lest_q_c)+find_Index_for_lest_Question_sl(".")+2
       while z<len(lest_q_c):
             for letter in lest_q_c[z]:
                 I_sample_question+=letter
             z+=1        
       I_main_question=""
       z=0
       y=len(lest_q_c)+find_Index_for_lest_Question_sl(".")
       while z<=y:
             for letter in lest_q_c[z]:
                 I_main_question+=letter
             z+=1
    main_Question.append(I_main_question)
    prompt.append(I_sample_question)
    QQdf="Dif�culty:"
    if(I_ID_K=="8391a002" or I_ID_K=="b1fab3e1" or I_ID_K=="b13378c8" or I_ID_K=="ca50de52"):
           ras="Diﬃculty"
           Deff_K=Taking_table[find_Index_for_Elements_And_Table(ras)+1]
           if(Deff_K=="■ □□"):
                I_Deff_K="Easy"
                difficulty.append(I_Deff_K)
           elif(Deff_K=="■■■"):
                I_Deff_K="Hard"
                difficulty.append(I_Deff_K)
           else:
               I_Deff_K="Medium"
               difficulty.append(I_Deff_K)

    else:
         I_Deff_K=Taking_table[find_Index_for_Elements_And_Table(QQdf)+1]
         if(I_Deff_K=="Easy"):
              difficulty.append(I_Deff_K)
         elif(I_Deff_K=="Hard"):
              difficulty.append(I_Deff_K)
         elif(I_Deff_K=="Medium"):
              difficulty.append(I_Deff_K)
         else:
            print(i)

    i+=1





data={'Question ID':id,'Domain':domain,'Skill':s_skill,'Question Difficulty':difficulty,'Question':main_Question,'Prompt':prompt,'Choice A':chose_a,'Choice_B':chose_b,'Choice_c':chose_c,'Choice_D':chose_d,'Correct Answer':correct_ans,'Explanation/Rationale':ans_reason}
df = pd.DataFrame(data)
excel_file_path=r'C:\Users\Vaishnavi\OneDrive\output.xlsx'

df.to_excel(excel_file_path,index=False)
print(f"Data saved to{df.to_excel}")
         