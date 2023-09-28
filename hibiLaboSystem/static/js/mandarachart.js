Chart.register(ChartDataLabels);

function createCanvas(className, array) {
    return new Chart(document.getElementById(className), {
        type: 'radar',
        data: {
            labels: ['', '', '', '', '', '', '', ''],
            datasets: [{
                label: '',
                data: [array[1], array[2], array[4], array[7], array[6], array[5], array[3], array[0]],
                borderColor: "#e2db9d",
                pointBackgroundColor: '#e2db9d',
            }]
        },
        options: {
            responsive: true,
            scales: {
                r: { // https://www.chartjs.org/docs/latest/axes/radial/
                    angleLines: {
                        color: '#cbcccd'
                    },
                    grid: {
                        color: '#cbcccd',
                    },
                    pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                        color: 'white'
                    },
                    ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                        color: 'none',
                        backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                    },
                    gridLines: {
                        color: "red",

                    },
                    min: 0,
                }
            },
            plugins: {
                legend: {
                    display: false, // キャプションを隠す
                },
                datalabels: {
                    display: false, // チャート上のデータ表示を非表示にする
                },
            },
            elements: {
                line: {
                    borderWidth: 2,

                },
                point: {
                    radius: 2, // 小さい方の円のサイズを設定します
                    borderWidth: 2, // 円の境界線の幅 円の境界線の幅
                }
            },
            tooltips: {
                enabled: false,
            },
            r: {

                //メモリ線
                ticks: {
                    display: false
                },
            }
        }
    });

}

function newArrayData(className) {

    const group = document.querySelectorAll(className);
    var newArray = [];
    group.forEach(item => {

        newArray.push(item.textContent);
    })
    return newArray;
}

function countValue(value1, value2) {

    const valueScore = document.querySelectorAll(".value-score")[value1];
    const textContent = parseInt(valueScore.textContent) + 1;
    valueScore.textContent = textContent;

    const valueScoreMain = document.querySelectorAll(".value-score")[value2];
    valueScoreMain.textContent = textContent;
}

function countValueCenter() {

    const textContentMain = document.querySelectorAll(".value-score");
    const valueContentMain = Number(textContentMain[4].textContent) + Number(textContentMain[5].textContent) + Number(textContentMain[6].textContent) + Number(textContentMain[7].textContent) + Number(textContentMain[9].textContent) + Number(textContentMain[10].textContent) + Number(textContentMain[11].textContent) + Number(textContentMain[12].textContent);
    textContentMain[8].textContent = valueContentMain
}

let arrayGroup1 = [];
let arrayGroup2 = [];
let arrayGroup3 = [];
let arrayGroup4 = [];
let arrayGroup5 = [];
let arrayGroup6 = [];
let arrayGroup7 = [];
let arrayGroup8 = [];

const group1 = document.querySelectorAll('.value-group-1');
group1.forEach(item => {

    arrayGroup1.push(item.textContent);
})

const group2 = document.querySelectorAll('.value-group-2');
group2.forEach(item => {

    arrayGroup2.push(item.textContent);
})

const group3 = document.querySelectorAll('.value-group-3');
group3.forEach(item => {

    arrayGroup3.push(item.textContent);
})

const group4 = document.querySelectorAll('.value-group-4');
group4.forEach(item => {

    arrayGroup4.push(item.textContent);
})

const group5 = document.querySelectorAll('.value-group-5');
group5.forEach(item => {

    arrayGroup5.push(item.textContent);
})

const group6 = document.querySelectorAll('.value-group-6');
group6.forEach(item => {

    arrayGroup6.push(item.textContent);
})

const group7 = document.querySelectorAll('.value-group-7');
group7.forEach(item => {

    arrayGroup7.push(item.textContent);
})

const group8 = document.querySelectorAll('.value-group-8');
group8.forEach(item => {

    arrayGroup8.push(item.textContent);
})

var mycanvas1 = createCanvas("mycanvas1", arrayGroup1);

var mycanvas2 = createCanvas("mycanvas2", arrayGroup2);

var mycanvas3 = createCanvas("mycanvas3", arrayGroup3);

var mycanvas4 = createCanvas("mycanvas4", arrayGroup4);

var mycanvas5 = createCanvas("mycanvas5", arrayGroup5);

var mycanvas6 = createCanvas("mycanvas6", arrayGroup6);

var mycanvas7 = createCanvas("mycanvas7", arrayGroup7);

var mycanvas8 = createCanvas("mycanvas8", arrayGroup8);

var mycanvas9 = createCanvas("mycanvas9", arrayGroup1);

var mycanvas10 = createCanvas("mycanvas10", arrayGroup2);

var mycanvas11 = createCanvas("mycanvas11", arrayGroup3);

var mycanvas12 = createCanvas("mycanvas12", arrayGroup4);

var mycanvas13 = createCanvas("mycanvas13", arrayGroup5);

var mycanvas14 = createCanvas("mycanvas14", arrayGroup6);

var mycanvas15 = createCanvas("mycanvas15", arrayGroup7);

var mycanvas16 = createCanvas("mycanvas16", arrayGroup8);


const valueElements = document.querySelectorAll('.value-table');
valueElements.forEach((element) => {

    element.classList.add("true")

    element.addEventListener('click', () => {

        element.classList.add('background-value-table');

        let child = element.querySelectorAll('span');

        const group1 = element.classList.contains("group1");
        const checkStatus = element.classList.contains("true");

        if (checkStatus) {

            $(child[0]).text(Number($(child[0]).text()) + 1);
            element.classList.remove("true");
            element.classList.add("false");

        } else {

            alert("押すのは 1 回のみ");
        }

        if (group1 && checkStatus) {

            countValue(0, 4);

            const newArray = newArrayData('.value-group-1');

            mycanvas1.destroy();
            mycanvas1 = createCanvas("mycanvas1", newArray);

            mycanvas9.destroy();
            mycanvas9 = createCanvas("mycanvas9", newArray);
        }

        const group2 = element.classList.contains("group2");
        if (group2 && checkStatus) {

            countValue(1, 5);

            const newArray = newArrayData('.value-group-2');

            mycanvas2.destroy();
            mycanvas2 = createCanvas("mycanvas2", newArray);

            mycanvas10.destroy();
            mycanvas10 = createCanvas("mycanvas10", newArray);

        }

        const group3 = element.classList.contains("group3");
        if (group3 && checkStatus) {

            countValue(2, 6);

            const newArray = newArrayData('.value-group-3');

            mycanvas3.destroy()
            mycanvas3 = createCanvas("mycanvas3", newArray)

            mycanvas11.destroy()
            mycanvas11 = createCanvas("mycanvas11", newArray)
        }

        const group4 = element.classList.contains("group4");
        if (group4 && checkStatus) {

            countValue(3, 7);

            const newArray = newArrayData('.value-group-4');

            mycanvas4.destroy()
            mycanvas4 = createCanvas("mycanvas4", newArray)

            mycanvas12.destroy()
            mycanvas12 = createCanvas("mycanvas12", newArray)
        }

        const group5 = element.classList.contains("group5");
        if (group5 && checkStatus) {

            countValue(13, 9);

            const newArray = newArrayData('.value-group-5');

            mycanvas5.destroy()
            mycanvas5 = createCanvas("mycanvas5", newArray)

            mycanvas13.destroy()
            mycanvas13 = createCanvas("mycanvas13", newArray)
        }

        const group6 = element.classList.contains("group6");
        if (group6 && checkStatus) {

            countValue(14, 10);

            const newArray = newArrayData('.value-group-6');

            mycanvas6.destroy()
            mycanvas6 = createCanvas("mycanvas6", newArray)

            mycanvas14.destroy()
            mycanvas14 = createCanvas("mycanvas14", newArray)
        }

        const group7 = element.classList.contains("group7");
        if (group7 && checkStatus) {

            countValue(15, 11);

            const newArray = newArrayData('.value-group-7');

            mycanvas7.destroy()
            mycanvas7 = createCanvas("mycanvas7", newArray)

            mycanvas15.destroy()
            mycanvas15 = createCanvas("mycanvas15", newArray)
        }

        const group8 = element.classList.contains("group8");
        if (group8 && checkStatus) {

            countValue(16, 12);

            const newArray = newArrayData('.value-group-8');

            mycanvas8.destroy()
            mycanvas8 = createCanvas("mycanvas8", newArray)

            mycanvas16.destroy()
            mycanvas16 = createCanvas("mycanvas16", newArray)
        }

        countValueCenter()
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

const choose = document.querySelectorAll(".choose");
choose[0].classList.add('background-tab-active')
choose[0].classList.add('color-print')
choose.forEach((element, index) => {
    element.addEventListener("click", function () {

        const listChoose = document.querySelectorAll(".choose");

        listChoose.forEach((item, count) => {
            if (index !== count) {

                item.classList.remove('background-tab-active')
                item.classList.remove('color-print')
            }
        })
        element.classList.add('background-tab-active')
        element.classList.add('color-print')
    })
})

console.log(window.innerWidth)