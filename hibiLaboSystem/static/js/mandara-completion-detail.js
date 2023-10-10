Chart.register(ChartDataLabels);

function createCanvas(className, array) {
    return new Chart(document.getElementById(className), {
        type: 'radar',
        data: {
            labels: ['', '', '', '', '', '', '', ''],
            datasets: [{
                label: '',
                data: [array[1], array[2], array[4], array[7], array[6], array[5], array[3], array[0]],
                borderColor: "#CB99C4",
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
                    borderWidth: 1,

                },
                point: {
                    radius: 1, // 小さい方の円のサイズを設定します
                    borderWidth: 1, // 円の境界線の幅 円の境界線の幅
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

function countValue(value1, value2, value3) {

    const valueScore = document.querySelectorAll(".value-score")[value1];
    const textContent = parseInt(valueScore.textContent) + 1;
    valueScore.textContent = textContent;

    const valueScoreMain = document.querySelectorAll(".value-score")[value2];
    valueScoreMain.textContent = textContent;

    document.querySelectorAll(".value-score-canvas")[value3].textContent = textContent;
}

function countValueCenter() {

    const textContentMain = document.querySelectorAll(".value-score");
    const valueContentMain = Number(textContentMain[4].textContent) + Number(textContentMain[5].textContent) + Number(textContentMain[6].textContent) + Number(textContentMain[7].textContent) + Number(textContentMain[9].textContent) + Number(textContentMain[10].textContent) + Number(textContentMain[11].textContent) + Number(textContentMain[12].textContent);
    textContentMain[8].textContent = valueContentMain;

    const valueTabCenter = document.querySelector(".value-vanvas-center");
    console.log("valueTabCenter", valueTabCenter);
    valueTabCenter.textContent = valueContentMain;
}

let arrayChartGroup1 = [];
let arrayChartGroup2 = [];
let arrayChartGroup3 = [];
let arrayChartGroup4 = [];
let arrayChartGroup5 = [];
let arrayChartGroup6 = [];
let arrayChartGroup7 = [];
let arrayChartGroup8 = [];

const group1 = document.querySelectorAll('.value-group-1');
group1.forEach(item => {

    arrayChartGroup1.push(item.textContent);
})

const group2 = document.querySelectorAll('.value-group-2');
group2.forEach(item => {

    arrayChartGroup2.push(item.textContent);
})

const group3 = document.querySelectorAll('.value-group-3');
group3.forEach(item => {

    arrayChartGroup3.push(item.textContent);
})

const group4 = document.querySelectorAll('.value-group-4');
group4.forEach(item => {

    arrayChartGroup4.push(item.textContent);
})

const group5 = document.querySelectorAll('.value-group-5');
group5.forEach(item => {

    arrayChartGroup5.push(item.textContent);
})

const group6 = document.querySelectorAll('.value-group-6');
group6.forEach(item => {

    arrayChartGroup6.push(item.textContent);
})

const group7 = document.querySelectorAll('.value-group-7');
group7.forEach(item => {

    arrayChartGroup7.push(item.textContent);
})

const group8 = document.querySelectorAll('.value-group-8');
group8.forEach(item => {

    arrayChartGroup8.push(item.textContent);
})

// var mycanvas1 = createCanvas("mycanvas1", arrayChartGroup1);

// var mycanvas2 = createCanvas("mycanvas2", arrayChartGroup2);

// var mycanvas3 = createCanvas("mycanvas3", arrayChartGroup3);

// var mycanvas4 = createCanvas("mycanvas4", arrayChartGroup4);

// var mycanvas5 = createCanvas("mycanvas5", arrayChartGroup5);

// var mycanvas6 = createCanvas("mycanvas6", arrayChartGroup6);

// var mycanvas7 = createCanvas("mycanvas7", arrayChartGroup7);

// var mycanvas8 = createCanvas("mycanvas8", arrayChartGroup8);

var mycanvas9 = createCanvas("mycanvas9", arrayChartGroup1);

var mycanvas10 = createCanvas("mycanvas10", arrayChartGroup2);

var mycanvas11 = createCanvas("mycanvas11", arrayChartGroup3);

var mycanvas12 = createCanvas("mycanvas12", arrayChartGroup4);

var mycanvas13 = createCanvas("mycanvas13", arrayChartGroup5);

var mycanvas14 = createCanvas("mycanvas14", arrayChartGroup6);

var mycanvas15 = createCanvas("mycanvas15", arrayChartGroup7);

var mycanvas16 = createCanvas("mycanvas16", arrayChartGroup8);

const valueElements = document.querySelectorAll('.value-table');
valueElements.forEach((element, index) => {

    const valueSpan = element.querySelector('span').textContent;
    if (valueSpan == 0) {
        element.querySelector('span').textContent = ""
    }

    const paragraph = element.querySelector('p').textContent;
    var content = `<div class="popup" id='popup${index + 1}'>
    <p class="title-popup">${paragraph}</p>
    <div class="wrapper-item">
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
        <div class="wrapper-text"></div>
    </div>
    </div>`;
    document.getElementById("value-body-bottom-left").innerHTML += content;
});

// const choose = document.querySelectorAll(".choose");
// choose[0].classList.add('background-choose-active')
// choose[0].classList.add('color-print')
// choose.forEach((element, index) => {
//     element.addEventListener("click", function () {

//         const listChoose = document.querySelectorAll(".choose");

//         listChoose.forEach((item, count) => {
//             if (index !== count) {

//                 item.classList.remove('background-choose-active')
//                 item.classList.remove('color-print')
//             }
//         })
//         element.classList.add('background-choose-active')
//         element.classList.add('color-print')

//         if (index === 1) {
//             console.log(document.querySelector(".body-bottom-left"));
//             document.querySelector(".masmas-mandara").style.display = "block";
//             document.querySelector(".body-bottom-left").style.display = "none";
//             document.querySelector(".body-bottom-right").style.display = "none";
//             document.querySelector(".content-title").style.display = "none";
//             document.querySelector(".text-title").textContent = "MASMAS MANDARA CHART";
//             document.querySelector(".wrapper-body-left").style.gridColumn = "span 12"
//         } else {
//             document.querySelector(".masmas-mandara").style.display = "none";
//             document.querySelector(".body-bottom-left").style.display = "grid";
//             document.querySelector(".body-bottom-right").style.display = "flex";
//             document.querySelector(".content-title").style.display = "block";
//             document.querySelector(".text-title").textContent = "MANDARA CHART";
//             document.querySelector(".wrapper-body-left").style.gridColumn = "span 8"
//         }
//     })
// })

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


console.log("a", window.innerWidth)
// 

const hiddenPopup = document.querySelectorAll(".container-fluid");
hiddenPopup.forEach(element => {

    element.addEventListener("click", function () {

        const popup = document.querySelectorAll(".popup")
        popup.forEach(itemPopup => {
            const checkStatus = itemPopup.classList.contains("hidden");
            if (checkStatus === false) {
                itemPopup.classList.add("hidden")
            }
        })
    })
})


var mouseDownTime = 0;
var minimumHoldTime = 1500;
let time = 0;
var timeoutId;

const popup = document.querySelectorAll('.popup');
popup.forEach(element => {
    element.classList.add("hidden")
})

const openPopup = document.querySelectorAll('.value-table');
openPopup.forEach((element, index) => {

    element.classList.add("true")
    element.addEventListener('mousedown', function (e) {
        e.preventDefault();
        mouseDownTime = new Date().getTime();
        const popup = document.querySelectorAll('.popup');
        popup.forEach(element => {
            element.classList.add("hidden")
        })
        time = 0;
        timeoutId = setTimeout(() => {
            document.getElementById(`popup${index + 1}`).classList.remove("hidden");
            time = 2;
        }, minimumHoldTime)

    });

    element.addEventListener("mouseup", function () {
        clearTimeout(timeoutId);
    })


    element.addEventListener('click', function (e) {
        e.stopPropagation(); // Ngăn sự kiện click lan ra ngoài
    });
})

// 

const barChart1 = document.getElementById('barChart1').getContext('2d');
const chart5 = new Chart(barChart1, {
    type: 'bar',
    data: {
        labels: ["2022/3", "2022/4", "2022/5", "2022/6", "2022/7", "2022/8", "2022/9"],
        datasets: [{
            label: '',
            data: [48, 53, 66, 78, 73, 70, 85],
            backgroundColor:
                '#C8C9CA',
        }]
    },
    options: {
        plugins: {


            datalabels: {
                anchor: 'end',
                align: 'top',
                offset: -5,
                color: "#2CAEB5",
                font: { size: 22, weight: 700 },
                formatter: function (value, context) {
                    return value;
                },

            },
            legend: {
                display: false,
            },
        },
        scales: {
            x: {
                grid: {
                    display: false
                },
                ticks: {
                    color: '#000000',

                }
            },
            y: {
                grid: {
                    display: false
                },
                ticks: {
                    color: '#000000',

                }
            }
        }
    },
});

// Giá trị Score ban đầu
let sumScore1 = 0;
let sumScore2 = 0;
let sumScore3 = 0;
let sumScore4 = 0;
let sumScore5 = 0;
let sumScore6 = 0;
let sumScore7 = 0;
let sumScore8 = 0;

arrayChartGroup1.forEach(element => {

    sumScore1 += Number(element)

})


arrayChartGroup2.forEach(element => {

    sumScore2 += Number(element)

})


arrayChartGroup3.forEach(element => {

    sumScore3 += Number(element)

})


arrayChartGroup4.forEach(element => {

    sumScore4 += Number(element)

})


arrayChartGroup5.forEach(element => {

    sumScore5 += Number(element)

})


arrayChartGroup6.forEach(element => {

    sumScore6 += Number(element)

})


arrayChartGroup7.forEach(element => {

    sumScore7 += Number(element)

})


arrayChartGroup8.forEach(element => {

    sumScore8 += Number(element)

})

const totalSumCore = [sumScore1, sumScore2, sumScore3, sumScore4, sumScore5, sumScore6, sumScore7, sumScore8]
document.querySelectorAll(".value-score-canvas")[0].textContent = sumScore1;

const valueScoreCanvas = document.querySelectorAll(".value-score-canvas");
valueScoreCanvas.forEach((element, index) => {

    element.textContent = totalSumCore[index];
})

document.querySelectorAll(".value-score")[0].textContent = totalSumCore[0]
document.querySelectorAll(".value-score")[4].textContent = totalSumCore[0]
document.querySelectorAll(".value-score")[1].textContent = totalSumCore[1]
document.querySelectorAll(".value-score")[5].textContent = totalSumCore[1]
document.querySelectorAll(".value-score")[2].textContent = totalSumCore[2]
document.querySelectorAll(".value-score")[6].textContent = totalSumCore[2]
document.querySelectorAll(".value-score")[3].textContent = totalSumCore[3]
document.querySelectorAll(".value-score")[7].textContent = totalSumCore[3]
document.querySelectorAll(".value-score")[9].textContent = totalSumCore[4]
document.querySelectorAll(".value-score")[13].textContent = totalSumCore[4]
document.querySelectorAll(".value-score")[10].textContent = totalSumCore[5]
document.querySelectorAll(".value-score")[14].textContent = totalSumCore[5]
document.querySelectorAll(".value-score")[11].textContent = totalSumCore[6]
document.querySelectorAll(".value-score")[15].textContent = totalSumCore[6]
document.querySelectorAll(".value-score")[12].textContent = totalSumCore[7]
document.querySelectorAll(".value-score")[16].textContent = totalSumCore[7]

countValueCenter()