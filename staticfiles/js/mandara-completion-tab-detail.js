Chart.register(ChartDataLabels);

function createCanvas(className, array) {
    return new Chart(document.getElementById(className), {
        type: 'radar',
        data: {
            labels: ['', '', '', '', '', '', '', ''],
            datasets: [{
                label: '',
                data: array,
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

function countValueCenter() {

    const textContentMain = document.querySelectorAll(".value-score");
    const valueContentMain = Number(textContentMain[4].textContent) + Number(textContentMain[5].textContent) + Number(textContentMain[6].textContent) + Number(textContentMain[7].textContent) + Number(textContentMain[9].textContent) + Number(textContentMain[10].textContent) + Number(textContentMain[11].textContent) + Number(textContentMain[12].textContent);
    textContentMain[8].textContent = valueContentMain;

    const valueTabCenter = document.querySelector(".value-vanvas-center");
    valueTabCenter.textContent = valueContentMain;
}

var mycanvas9 = createCanvas("mycanvas1", arrayChartGroupF);

var mycanvas10 = createCanvas("mycanvas2", arrayChartGroupC);

var mycanvas11 = createCanvas("mycanvas3", arrayChartGroupG);

var mycanvas12 = createCanvas("mycanvas4", arrayChartGroupB);

var mycanvas13 = createCanvas("mycanvas5", arrayChartGroupD);

var mycanvas14 = createCanvas("mycanvas6", arrayChartGroupE);

var mycanvas15 = createCanvas("mycanvas7", arrayChartGroupA);

var mycanvas16 = createCanvas("mycanvas8", arrayChartGroupH);

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

countValueCenter()