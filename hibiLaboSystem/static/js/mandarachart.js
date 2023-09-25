
const valueElements = document.querySelectorAll('.value-table');
valueElements.forEach((element) => {
    element.classList.add("true")
    element.addEventListener('click', () => {

        // const spanElemen 
        // spanElement.textContent = parseInt(spanElement.textContent) + 1;
        element.classList.add('background-value-table');

        let child = element.querySelectorAll('span');

        const group1 = element.classList.contains("group1");
        const checkStatus = element.classList.contains("true");

        let array = [];
        if (checkStatus) {

            $(child[0]).text(Number($(child[0]).text()) + 1)
            element.classList.remove("true")
            element.classList.add("false")

        } else {

            alert("押すのは 1 回のみ")
        }
        if (group1 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[0];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[4];
            valueScoreMain.textContent = textContent;


            array.push(textContent);

        }

        const group2 = element.classList.contains("group2");
        if (group2 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[1];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[5];
            valueScoreMain.textContent = textContent;

            array.push(textContent);
        }

        const group3 = element.classList.contains("group3");
        if (group3 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[2];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[6];
            valueScoreMain.textContent = textContent;

            array.push(textContent);
        }

        const group4 = element.classList.contains("group4");
        if (group4 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[3];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[7];
            valueScoreMain.textContent = textContent;

            array.push(textContent);
        }

        const group5 = element.classList.contains("group5");
        if (group5 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[13];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[9];
            valueScoreMain.textContent = textContent;

            array.push(textContent);
        }

        const group6 = element.classList.contains("group6");
        if (group6 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[14];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[10];
            valueScoreMain.textContent = textContent;

            array.push(textContent);
        }

        const group7 = element.classList.contains("group7");
        if (group7 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[15];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[11];
            valueScoreMain.textContent = textContent;

            array.push(textContent);
        }

        const group8 = element.classList.contains("group8");
        if (group8 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[16];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[12];
            valueScoreMain.textContent = textContent;

            array.push(textContent);
        }

        const textContentMain = document.querySelectorAll(".value-score");
        const valueContentMain = Number(textContentMain[4].textContent) + Number(textContentMain[5].textContent) + Number(textContentMain[6].textContent) + Number(textContentMain[7].textContent) + Number(textContentMain[9].textContent) + Number(textContentMain[10].textContent) + Number(textContentMain[11].textContent) + Number(textContentMain[12].textContent);

        textContentMain[8].textContent = valueContentMain
    });
});


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
console.log(window.innerWidth)