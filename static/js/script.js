const BtnLogin = document.getElementById('BtnLogin');
const BtnReset = document.getElementById('BtnReset');

const Div1Part1 = document.getElementById('Div1-Part1');
const Div1Part1Header = document.getElementById('Div1-Part1-Header');

const MyBody = document.getElementById('MyBody');
const Phase1_Overlay = document.getElementById('Phase1_Overlay');
const Phase2_Overlay = document.getElementById('Phase2_Overlay');
const Phase3_Overlay = document.getElementById('Phase3_Overlay');
const Phase4_Overlay = document.getElementById('Phase4_Overlay');
const Phase5_Overlay = document.getElementById('Phase5_Overlay');
const Phase6_Overlay = document.getElementById('Phase6_Overlay');
const Phase7_Overlay = document.getElementById('Phase7_Overlay');
const Phase8_Overlay = document.getElementById('Phase8_Overlay');
const Phase9_Overlay = document.getElementById('Phase9_Overlay');
const Phase10_Overlay = document.getElementById('Phase10_Overlay');

const MyForm = document.getElementById('MyForm');
const DeleteBtn = document.getElementById('DeleteBtn');


    function myFunction() {
        document.getElementById("BtnReset").style.backgroundColor = "red";
      }


    function myFunctionUp() {
      document.getElementById("Div1-Part1").style.opacity= 0.7;
        
      }  
    

      function myFunctionDown() {
        document.getElementById("Div1-Part1").style.opacity= 1;
      }  
      
 
     function myFunctionUp2() {
        document.getElementById("Div1-Part2").style.opacity= 0.7;
          
        }  
      
  
     function myFunctionDown2() {
          document.getElementById("Div1-Part2").style.opacity= 1;
        }  
          

     function myFunctionUp3() {
          document.getElementById("Div1-Part3").style.opacity= 0.7;
            
          }  
        
    
     function myFunctionDown3() {
            document.getElementById("Div1-Part3").style.opacity= 1;
          }  
             
 
     function myFunctionUp4() {
            document.getElementById("Div2-Part1").style.opacity= 0.7;
              
            } 
          
      
     function myFunctionDown4() {
              document.getElementById("Div2-Part1").style.opacity= 1;
            }  
              
            
     function myFunctionUp5() {
              document.getElementById("Div2-Part2").style.opacity= 0.7;
                
              }  
            
        
     function myFunctionDown5() {
              document.getElementById("Div2-Part2").style.opacity= 1;
              }  


     function myFunctionUp6() {
                document.getElementById("Div2-Part3").style.opacity= 0.7;
                  
                }  
              
          
     function myFunctionDown6() {
                  document.getElementById("Div2-Part3").style.opacity= 1;
                }  

     function myFunctionBody(){
                  document.getElementById('Phase1_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase1_Overlay').style.height="70%";                  
                  document.getElementById('Phase1_Overlay').style.transition="1s";

                  document.getElementById('Phase2_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase2_Overlay').style.height="50%";                  
                  document.getElementById('Phase2_Overlay').style.transition="1s";

                  document.getElementById('Phase3_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase3_Overlay').style.height="30%";                  
                  document.getElementById('Phase3_Overlay').style.transition="1s";

                  document.getElementById('Phase4_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase4_Overlay').style.height="20%";                  
                  document.getElementById('Phase4_Overlay').style.transition="1s";

                  document.getElementById('Phase5_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase5_Overlay').style.height="50%";                  
                  document.getElementById('Phase5_Overlay').style.transition="1s";

                  document.getElementById('Phase6_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase6_Overlay').style.height="50%";                  
                  document.getElementById('Phase6_Overlay').style.transition="1s";

                  document.getElementById('Phase7_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase7_Overlay').style.height="20%";                  
                  document.getElementById('Phase7_Overlay').style.transition="1s";

                  document.getElementById('Phase8_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase8_Overlay').style.height="30%";                  
                  document.getElementById('Phase8_Overlay').style.transition="1s";

                  document.getElementById('Phase9_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase9_Overlay').style.height="40%";                  
                  document.getElementById('Phase9_Overlay').style.transition="1s";

                  document.getElementById('Phase10_Overlay').style.backgroundColor="red";
                  document.getElementById('Phase10_Overlay').style.height="10%";                  
                  document.getElementById('Phase10_Overlay').style.transition="1s";
     }  
     
     



     document.getElementById('DeleteBtn').onclick = function Del() {
      MyForm.reset(); // Réinitialise tous les champs du formulaire
  };     
    

