Chart.register(ChartDataLabels);

function daysInThisMonth() {
  var now = new Date();
  return new Date(now.getFullYear(), now.getMonth()+1, 0).getDate();
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

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
    valueTabCenter.textContent = valueContentMain;
}

var mycanvas1 = createCanvas("mycanvas1", arrayChartGroupF);

var mycanvas2 = createCanvas("mycanvas2", arrayChartGroupC);

var mycanvas3 = createCanvas("mycanvas3", arrayChartGroupG);

var mycanvas4 = createCanvas("mycanvas4", arrayChartGroupB);

var mycanvas5 = createCanvas("mycanvas5", arrayChartGroupD);

var mycanvas6 = createCanvas("mycanvas6", arrayChartGroupE);

var mycanvas7 = createCanvas("mycanvas7", arrayChartGroupA);

var mycanvas8 = createCanvas("mycanvas8", arrayChartGroupH);

const valueElements = document.querySelectorAll('.value-table');
valueElements.forEach((element, index) => {

    const valueSpan = element.querySelector('span').textContent;

    const paragraph = element.querySelector('p').textContent;
    var content = `<div class="popup" id='popup${index + 1}'>
    <p class="title-popup">${paragraph}</p>
    <div class="wrapper-item">`;
    for (var i = 0; i < daysInThisMonth(); i++) {
        content += `<div class="wrapper-text text-center">${i + 1}</div>`;
    }
    content += `</div>
            </div>`;
    document.getElementById("value-body-bottom-left").innerHTML += content;
});

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

        if (index === 1) {
            document.querySelector(".masmas-mandara").style.display = "block";
            document.querySelector(".body-bottom-left").style.display = "none";
            document.querySelector(".body-bottom-right").style.display = "none";
            document.querySelector(".content-title").style.display = "none";
            document.querySelector(".text-title").textContent = "MASMAS MANDARA CHART";
            document.querySelector(".wrapper-body-left").style.gridColumn = "span 12"
        } else {
            document.querySelector(".masmas-mandara").style.display = "none";
            document.querySelector(".body-bottom-left").style.display = "grid";
            document.querySelector(".body-bottom-right").style.display = "flex";
            document.querySelector(".content-title").style.display = "block";
            document.querySelector(".text-title").textContent = "MANDARA CHART";
            document.querySelector(".wrapper-body-left").style.gridColumn = "span 8"
        }
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

    // element.classList.add("true")
    element.addEventListener('mousedown', function (e) {
        e.preventDefault();
        mouseDownTime = new Date().getTime();
        const popup = document.querySelectorAll('.popup');
        popup.forEach(element => {
            element.classList.add("hidden")
        })
        time = 0;
        timeoutId = setTimeout(() => {
            fetch(urlGet + `?type_box=${element.dataset.boxType}`, {
              method: "GET",
              headers: {
                "X-Requested-With": "XMLHttpRequest",
              }
            })
            .then(response => response.json())
            .then(data => {
                let popup = document.getElementById(`popup${index + 1}`);
                if(data.context) {
                    popup.querySelector('.wrapper-item').innerHTML = '';
                    let contentHtml = ''
                    for (var i = 0; i < daysInThisMonth(); i++) {
                        let find = data.context.find(item => item.day == i + 1);
                        let active = find[element.dataset.boxType+'_result'] == 1 ? 'active' : '';
                        contentHtml += `<div class="wrapper-text text-center ${active}">${i + 1}</div>`;
                    }
                    popup.querySelector('.wrapper-item').innerHTML = contentHtml;
                }
                popup.classList.remove("hidden");
                time = 2;
            });
        }, minimumHoldTime)

    });

    element.addEventListener("mouseup", function () {
        clearTimeout(timeoutId);
    })


    element.addEventListener('click', function (e) {
        e.stopPropagation(); // Ngăn sự kiện click lan ra ngoài

        if (time < 2) {
            let child = element.querySelectorAll('span');

            const group1 = element.classList.contains("group1");
            const group2 = element.classList.contains("group2");
            const group3 = element.classList.contains("group3");
            const group4 = element.classList.contains("group4");
            const group5 = element.classList.contains("group5");
            const group6 = element.classList.contains("group6");
            const group7 = element.classList.contains("group7");
            const group8 = element.classList.contains("group8");
            const checkStatus = element.classList.contains("true");

            if (checkStatus) {
                fetch(urlPost, {
                  method: "POST",
                  credentials: "same-origin",
                  headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCookie("csrftoken"),
                  },
                  body: JSON.stringify({box: element.dataset.boxType})
                })
                .then(response => response.json())
                .then(data => {
                  console.log(data);
                  if(data.status && data.status == 'OK'){
                    $(child[0]).text(Number($(child[0]).text()) + 1);
                    element.classList.add('background-value-table');
                    element.classList.remove("true");
                    element.classList.add("false");

                    if (group1) {

                        countValue(0, 4, 0);

                        const newArray = newArrayData('.value-group-1');

                        mycanvas1.destroy();
                        mycanvas1 = createCanvas("mycanvas1", newArray);

                    }

                    if (group2) {

                        countValue(1, 5, 1);

                        const newArray = newArrayData('.value-group-2');

                        mycanvas2.destroy();
                        mycanvas2 = createCanvas("mycanvas2", newArray);
                    }

                    if (group3) {

                        countValue(2, 6, 2);

                        const newArray = newArrayData('.value-group-3');

                        mycanvas3.destroy()
                        mycanvas3 = createCanvas("mycanvas3", newArray)

                    }

                    if (group4) {

                        countValue(3, 7, 3);

                        const newArray = newArrayData('.value-group-4');

                        mycanvas4.destroy()
                        mycanvas4 = createCanvas("mycanvas4", newArray)

                    }

                    if (group5) {

                        countValue(13, 9, 4);

                        const newArray = newArrayData('.value-group-5');

                        mycanvas5.destroy()
                        mycanvas5 = createCanvas("mycanvas5", newArray)

                    }

                    if (group6) {

                        countValue(14, 10, 5);

                        const newArray = newArrayData('.value-group-6');

                        mycanvas6.destroy()
                        mycanvas6 = createCanvas("mycanvas6", newArray)
                    }

                    if (group7) {

                        countValue(15, 11, 6);

                        const newArray = newArrayData('.value-group-7');

                        mycanvas7.destroy()
                        mycanvas7 = createCanvas("mycanvas7", newArray)
                    }

                    if (group8) {

                        countValue(16, 12, 7);

                        const newArray = newArrayData('.value-group-8');

                        mycanvas8.destroy()
                        mycanvas8 = createCanvas("mycanvas8", newArray)
                    }

                    countValueCenter();
                    values[values.length - 1] += 1;
                    char5.destroy();
                    char5 = createBarChart(labels, values); 
                  }
                });

            }
        }

    });
})

// 
function createBarChart(arr_label, arr_value) {
    const barChart1 = document.getElementById('barChart1').getContext('2d');
    return new Chart(barChart1, {
        type: 'bar',
        data: {
            labels: arr_label,
            datasets: [{
                label: '',
                data: arr_value,
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
                    max: Math.max(...values) + 1,
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#000000',

                    }
                },
            }
        },
    });    
}

var char5 = createBarChart(labels, values);