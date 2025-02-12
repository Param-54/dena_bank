function myvalid(){
    var ph_val = document.getElementById("ph").value;
    let ph_len=ph_val.length;
    if (ph_len != 10){
        // document.write("Pl enter 10 digit mobile no");
        //document.getElementById("res").innerHTML="Pl enter 10 digit mobile no";
        document.getElementById("ph_lb").innerHTML="Pl enter 10 digit mobile new no";
    } else {
        document.getElementById("ph_lb").innerHTML=" ";
    }
}

function nmval1(){
    //alert("Saved ");
    //console.log("vlick");
    document.getElementById("sv").innerHTML="Data saved";
}

function nmval2(){
     alert("Saved  nmval2");
    //console.log("vlick");
    //document.getElementById("sv").innerHTML="Data saved";
}

function mem_name(){
    let mes="saved"
    alert(mes);
   //console.log("vlick");
   //document.getElementById("sv").innerHTML="Data saved";
}


    
// function mem_nm_check() {
//     let memnm_val = document.getElementById("mem_nm").value;
//     pattern=[A-Za-z];
//         if (pattern.test(memnm_val) == false){
//             document.getElementById("name_chk").innerHTML = "Name contain only alpha ";
//         }
//     }

    // for (let x_val of memid_val){
    //     if (x_val >=0 && x_val<=9){
    //         document.getElementById("nm_chk").innerHTML = "" ;
    //         continue;
    //         //console.log("ok");
    //     }else{
    //         document.getElementById("nm_chk").innerHTML = "Only Numeric values";
    //         break;
    //     }
    //    }
        
     
    // alert(memid_val);



