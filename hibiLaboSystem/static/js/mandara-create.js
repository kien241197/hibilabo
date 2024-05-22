
const OPTION_LIST = [
    [6, 48, 55],
    [3, 24, 31],
    [1, 8, 15],
    [4, 32, 39],
    [5, 40, 47],
    [0, 0, 7],
    [2, 16, 23],
    [7, 56, 64],
];
const sort_fields = ['start_YYYYMM', 'end_YYYYMM', 'A_keyword', 'A_dueto', 'B_keyword', 'B_dueto', 'C_keyword', 'C_dueto',
    'D_keyword', 'D_dueto', 'E_keyword', 'E_dueto', 'F_keyword', 'F_dueto', 'G_keyword', 'G_dueto', 'H_keyword', 'H_dueto',
    'A1_content', 'A2_content', 'A3_content', 'A4_content', 'A5_content', 'A6_content', 'A7_content', 'A8_content',
    'B1_content', 'B2_content', 'B3_content', 'B4_content', 'B5_content', 'B6_content', 'B7_content', 'B8_content',
    'C1_content', 'C2_content', 'C3_content', 'C4_content', 'C5_content', 'C6_content', 'C7_content', 'C8_content',
    'D1_content', 'D2_content', 'D3_content', 'D4_content', 'D5_content', 'D6_content', 'D7_content', 'D8_content',
    'E1_content', 'E2_content', 'E3_content', 'E4_content', 'E5_content', 'E6_content', 'E7_content', 'E8_content',
    'F1_content', 'F2_content', 'F3_content', 'F4_content', 'F5_content', 'F6_content', 'F7_content', 'F8_content',
    'G1_content', 'G2_content', 'G3_content', 'G4_content', 'G5_content', 'G6_content', 'G7_content', 'G8_content',
    'H1_content', 'H2_content', 'H3_content', 'H4_content', 'H5_content', 'H6_content', 'H7_content', 'H8_content',
];
if(flg_finished === true){

    console.log("vaof dday")
    sort_fields.some(item => {
		$(`#id_${item}`).attr("required", true);
	})
}
const choose = document.querySelectorAll(".choose");
choose[0].classList.add('background-choose-active')
choose[0].classList.add('color-print')
choose.forEach((element, index) => {
    element.addEventListener("click", function () {

        const listChoose = document.querySelectorAll(".choose");

        listChoose.forEach((item, count) => {
            if (index !== count) {

                item.classList.remove('background-choose-active')
                item.classList.remove('color-print')
            }
        })
        element.classList.add('background-choose-active')
        element.classList.add('color-print')
    })
})

// const valueTab1 = document.querySelector(".tab1");
// document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.add("hidden-tab");
// document.querySelector(".tab1").classList.add("background-tab-active")
// valueTab1.addEventListener('click', () => {
//     valueTab1.classList.add('background-tab-active');
//     document.querySelector(".tab2").classList.remove("background-tab-active")
//     document.querySelector(".wrapper-item-table-body-bottom-right-tab-1").classList.remove("hidden-tab");
//     document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.add("hidden-tab");
// });

// const valueTab2 = document.querySelector(".tab2");
// valueTab2.addEventListener('click', () => {
//     valueTab2.classList.add('background-tab-active');
//     document.querySelector(".tab1").classList.remove("background-tab-active")
//     document.querySelector(".wrapper-item-table-body-bottom-right-tab-1").classList.add("hidden-tab");
//     document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.remove("hidden-tab");
// });

console.log({flg_finished});
// 
const buttonTitle = document.getElementById('button-title-1');
if (buttonTitle) {
    buttonTitle.addEventListener("click", function () {
        document.getElementById('id_total_mission').value = '';
        const valueInput = document.querySelectorAll(".input-table");
        const inputValueTab = document.querySelectorAll(".input-value-tab");
        const titleValueTableScore = document.querySelectorAll(".title-value-table-score");
        const titleMainScore = document.querySelectorAll(".title-main-score");
        const timeSelects = document.querySelectorAll(".select");
        valueInput.forEach(element => {
            if (element.value) {
                element.value = "";
            }
        });

        inputValueTab.forEach(element => {
            if (element.value) {
                element.value = "";
            }
        })

        titleValueTableScore.forEach(element => {
            if (element.textContent) {
                element.textContent = "";
            }
        })

        titleMainScore.forEach(element => {

            if (element.textContent) {

                element.textContent = ""
            }
        })

        timeSelects.forEach(element => {
            element.value = "";
        })
    })
}

// 
const inputValue = document.querySelectorAll('.input-table');

const inputValueTab = document.querySelectorAll(".input-value-tab");
inputValueTab.forEach((element, index) => {

    render_keyword(index, element.value);
    element.addEventListener('change', function () {
        render_keyword(index, element.value);
    })
})


const inputValueSocre = document.querySelector('.input-value-score')
function render_keyword(numb, value) {
    document.querySelectorAll(".title-main-score")[OPTION_LIST[numb][0]].textContent = value;
    document.querySelectorAll(".title-value-table-score")[OPTION_LIST[numb][0]].textContent = value;
}

function selectEndDate() {
    document.getElementById("id_end_YYYYMM").value = document.getElementById("id_start_YYYYMM").value
}

$(document).ready(function () {

    if ($("#id_A_keyword").val() && $("#id_B_keyword").val() && $("#id_C_keyword").val() && $("#id_D_keyword").val() && $("#id_E_keyword").val() && $("#id_F_keyword").val() && $("#id_G_keyword").val() && $("#id_H_keyword").val()) {
        $(".wrapper-top-block").css("display", "none")
        $(".title-main-score-top").css("display", "none")
    }

    $('body').keydown(function (e) {
        if (e.which === 9) { // Tab key code is 9
            let index = sort_fields.indexOf($(e.target).attr('name'));
            if (sort_fields[index]) {
                if ($(e.target).val()) {
                    $(`#id_${sort_fields[index]}`).removeClass('box-required');
                    if ($(`#id_${sort_fields[index + 1]}`).attr("disabled")) {
                        $(`#id_${sort_fields[index + 1]}`).removeAttr("disabled");
                        $(`#id_${sort_fields[index + 1]}`).addClass('box-required');
                        $('#id_field_stop').val(sort_fields[index + 1]);
                    }
                    $(`#id_${sort_fields[index + 1]}`).select(); // Select the text inside the input
                } else {
                    $(`#id_${sort_fields[index]}`).select(); // Select the text inside the input
                }
                e.preventDefault(); // Prevent default tab behavior       
            }
        }
    });
});