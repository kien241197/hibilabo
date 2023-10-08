
const OPTION_LIST = [
    [0,0,7],
    [1,8,15],
    [2,16,23],
    [4,32,39],
    [7,56,64],
    [6,48,55],
    [5,40,47],
    [3,24,31],
];
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

const valueTab1 = document.querySelector(".tab1");
document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.add("hidden-tab");
document.querySelector(".tab1").classList.add("background-tab-active")
valueTab1.addEventListener('click', () => {
    valueTab1.classList.add('background-tab-active');
    document.querySelector(".tab2").classList.remove("background-tab-active")
    document.querySelector(".wrapper-item-table-body-bottom-right-tab-1").classList.remove("hidden-tab");
    document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.add("hidden-tab");
});

// const valueTab2 = document.querySelector(".tab2");
// valueTab2.addEventListener('click', () => {
//     valueTab2.classList.add('background-tab-active');
//     document.querySelector(".tab1").classList.remove("background-tab-active")
//     document.querySelector(".wrapper-item-table-body-bottom-right-tab-1").classList.add("hidden-tab");
//     document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.remove("hidden-tab");
// });


// 
const buttonTitle = document.getElementById('button-title-1');
buttonTitle.addEventListener("click", function () {

    const valueInput = document.querySelectorAll(".input-table");
    const inputValueTab = document.querySelectorAll(".input-value-tab");
    const titleValueTableScore = document.querySelectorAll(".title-value-table-score");
    const titleMainScore = document.querySelectorAll(".title-main-score");
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
})

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
console.log(window.innerWidth)