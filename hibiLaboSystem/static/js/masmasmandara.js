
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

const valueTab2 = document.querySelector(".tab2");
valueTab2.addEventListener('click', () => {
    valueTab2.classList.add('background-tab-active');
    document.querySelector(".tab1").classList.remove("background-tab-active")
    document.querySelector(".wrapper-item-table-body-bottom-right-tab-1").classList.add("hidden-tab");
    document.querySelector(".wrapper-item-table-body-bottom-right-tab-2").classList.remove("hidden-tab");
});


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

const inputValueTab = document.querySelectorAll(".input-value-tab");
inputValueTab.forEach((element, index) => {

    element.addEventListener('change', function () {

        if (index === 0) {

            document.querySelectorAll(".title-main-score")[0].textContent = element.value
            document.querySelectorAll(".title-value-table-score")[0].textContent = element.value
        }

        if (index === 1) {

            document.querySelectorAll(".title-main-score")[1].textContent = element.value
            document.querySelectorAll(".title-value-table-score")[1].textContent = element.value
        }

        if (index === 2) {

            document.querySelectorAll(".title-main-score")[2].textContent = element.value
            document.querySelectorAll(".title-value-table-score")[2].textContent = element.value
        }

        if (index === 3) {

            document.querySelectorAll(".title-main-score")[3].textContent = element.value
            document.querySelectorAll(".title-value-table-score")[3].textContent = element.value
        }

        if (index === 4) {

            document.querySelectorAll(".title-main-score")[4].textContent = element.value
            document.querySelectorAll(".title-value-table-score")[4].textContent = element.value
        }

        if (index === 5) {

            document.querySelectorAll(".title-main-score")[5].textContent = element.value
            document.querySelectorAll(".title-value-table-score")[5].textContent = element.value
        }

        if (index === 6) {

            document.querySelectorAll(".title-main-score")[6].textContent = element.value
            document.querySelectorAll(".title-value-table-score")[6].textContent = element.value
        }

        if (index === 7) {

            document.querySelectorAll(".title-main-score")[7].textContent = element.value
            document.querySelectorAll(".title-value-table-score")[7].textContent = element.value
        }
    })
})

console.log(window.innerWidth)