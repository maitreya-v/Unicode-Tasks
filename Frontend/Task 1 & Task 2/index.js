
      function validate(){
    var name1=document.getElementById("text1").value;
    var email1=document.getElementById("text2").value;
    var phoneno1=document.getElementById("text3").value;
    var message1=document.getElementById("text4").value;
    var regxForName=/^([a-zA-Z]{3,20})$/;
    var regxForEmail= /^([a-z0-9\.-]+)@([a-z0-9-]+).([a-z]{2,8})(.[a-z]{2,8})?$/;
    var regxForPhoneNo=/^([0-9]{10})$/;
    var regxForMessage=/^([a-zA-Z0-9\.]{1,100})$/;
     
  jaja=true
  if(!regxForName.test(name1)){
    document.getElementById("label1").innerHTML="INVALID";
    document.getElementById("label1").style.visibility="visible";
    document.getElementById("label1").style.color="red";
    jaja=false
  }
  else{
    document.getElementById("label1").style.visibility="hidden";
  }
  
            if(!regxForEmail.test(email1)){
              document.getElementById("label2").innerHTML="INVALID";
                document.getElementById("label2").style.color="red";
                document.getElementById("label2").style.visibility="visible";
                jaja=false
            }
            else{
    document.getElementById("label2").style.visibility="hidden";
  }
           
            if(!regxForPhoneNo.test(phoneno1)){
              document.getElementById("label3").innerHTML="INVALID";
                document.getElementById("label3").style.color="red";
                document.getElementById("label3").style.visibility="visible";
                jaja=false
            }
            else{
    document.getElementById("label3").style.visibility="hidden";
  }
            if(!regxForMessage.test(message1)){
              document.getElementById("label4").innerHTML="INVALID.Cannot be empty";
                document.getElementById("label4").style.color="red";
                document.getElementById("label4").style.visibility="visible";
                jaja=false
            } 
            else{
    document.getElementById("label4").style.visibility="hidden";
  }
if(jaja==true){
  document.getElementById("formBtn").type="submit"
}

         
}
let userHasScrolled=false;
window.addEventListener ('scroll',(e)=>{
  if(window.scrollY==0){
    document.getElementById('mainNavbar').style.backgroundColor='transparent'
  }
  else{
   userHasScrolled=true;
   document.getElementById('mainNavbar').style.background='#f7b3b0';
   document.getElementById('mainNavbar').style.transition='background 200ms';
  }
})  