//チェックマークのカウント
function func_count(){
    var mytable = document.getElementById("table_result");
    var resulttable = document.getElementById("calc_resul");
    var stra = document.getElementById("id_concept_type_a");
    var strb = document.getElementById("id_concept_type_b");
    var strc = document.getElementById("id_concept_type_c");
    var strd = document.getElementById("id_concept_type_d");
    var stre = document.getElementById("id_concept_type_e");

    var int_counter = 0;
    let elm = document.getElementsByClassName("a");
    for (let i = 0; i < elm.length; i++) {
        if (elm[i].checked){
            int_counter++;
        }
    }
    mytable.rows[1].cells[1].innerHTML = int_counter;
    stra.value = int_counter;

    var int_counter = 0;
    elm = document.getElementsByClassName("b");
    for (let i = 0; i < elm.length; i++) {
        if (elm[i].checked){
            int_counter++;
        }
    }
    mytable.rows[2].cells[1].innerHTML = int_counter;
    strb.value = int_counter;

    var int_counter = 0;
    elm = document.getElementsByClassName("c");
    for (let i = 0; i < elm.length; i++) {
        if (elm[i].checked){
            int_counter++;
        }
    }
    mytable.rows[3].cells[1].innerHTML = int_counter;
    strc.value = int_counter;

    var int_counter = 0;
    elm = document.getElementsByClassName("d");
    for (let i = 0; i < elm.length; i++) {
        if (elm[i].checked){
            int_counter++;
        }
    }
    mytable.rows[4].cells[1].innerHTML = int_counter;
    strd.value = int_counter;

    var int_counter = 0;
    elm = document.getElementsByClassName("e");
    for (let i = 0; i < elm.length; i++) {
        if (elm[i].checked){
            int_counter++;
        }
    }
    mytable.rows[5].cells[1].innerHTML = int_counter;
    stre.value = int_counter;

}
function func_readonly(){
    var flg_finished = document.getElementById("id_flg_finished");
    //提出フラグがtrueの時には、編集ができないようにする
    if (flg_finished.checked){
        for ( var i=1; i <= 25; i++){
            strid = '[id="id_concept_q' +  i + '"]'
            document.querySelector(strid).addEventListener('click', (event) => {
            event.target.checked = !event.target.checked;
            });
        }

        document.querySelector('[id="id_flg_wordpress"]').addEventListener('click', (event) => {
        event.target.checked = !event.target.checked;
        });
        target = document.getElementById("id_concept_comment");
        target.readOnly = true;
    }
}
