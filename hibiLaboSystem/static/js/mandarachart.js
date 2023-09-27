Chart.register(ChartDataLabels);

var arrayGroup1 = [];
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



var mycanvas1 = new Chart(document.getElementById("mycanvas1"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup1,
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

                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas2 = new Chart(document.getElementById("mycanvas2"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup2,
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

                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas3 = new Chart(document.getElementById("mycanvas3"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup3,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {

        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas4 = new Chart(document.getElementById("mycanvas4"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup4,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {

        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas5 = new Chart(document.getElementById("mycanvas5"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup5,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {

        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas6 = new Chart(document.getElementById("mycanvas6"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup6,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {

        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas7 = new Chart(document.getElementById("mycanvas7"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup7,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {

        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas8 = new Chart(document.getElementById("mycanvas8"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup8,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {

        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas9 = new Chart(document.getElementById("mycanvas9"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup1,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',
        }]
    },
    options: {
        responsive: true,
        aspectRatio: 1,
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

                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas10 = new Chart(document.getElementById("mycanvas10"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup2,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {
        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,
            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas11 = new Chart(document.getElementById("mycanvas11"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup3,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {
        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas12 = new Chart(document.getElementById("mycanvas12"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup4,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {
        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas13 = new Chart(document.getElementById("mycanvas13"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup5,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',

        }]
    },
    options: {
        scales: {
            r: { // https://www.chartjs.org/docs/latest/axes/radial/
                angleLines: {
                    color: '#cbcccd'
                },
                grid: {
                    color: '#cbcccd'
                },
                pointLabels: { // https://www.chartjs.org/docs/latest/axes/radial/#point-labels
                    color: 'white'
                },
                ticks: { // https://www.chartjs.org/docs/latest/axes/radial/#ticks
                    color: 'none',
                    backdropColor: 'transparent' // https://www.chartjs.org/docs/latest/axes/_common_ticks.html
                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 2,

            },
            point: {
                radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 2, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas14 = new Chart(document.getElementById("mycanvas14"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup6,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',
        }]
    },
    options: {
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

                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 1,

            },
            point: {
                radius: 1, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 1, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas15 = new Chart(document.getElementById("mycanvas15"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup7,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',
        }]
    },
    options: {
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

                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 1,

            },
            point: {
                radius: 1, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 1, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});

var mycanvas16 = new Chart(document.getElementById("mycanvas16"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: arrayGroup8,
            borderColor: "#e2db9d",
            pointBackgroundColor: '#e2db9d',
        }]
    },
    options: {
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

                }
            }
        },
        plugins: {
            legend: {
                display: false, // Ẩn chú thích (legend)
            },
            datalabels: {
                display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
            },
        },
        elements: {
            line: {
                borderWidth: 1,

            },
            point: {
                radius: 1, // Đặt kích thước của hình tròn nhỏ hơn
                borderWidth: 1, // Độ rộng của viền hình tròn
            }
        },
        tooltips: {
            enabled: false,
        },
    }
});


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
            mycanvas1.destroy();
            const valueScore = document.querySelectorAll(".value-score")[0];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[4];
            valueScoreMain.textContent = textContent;


            const group = document.querySelectorAll('.value-group-1');
            let newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })

            mycanvas1 = new Chart(document.getElementById("mycanvas1"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

            mycanvas9.destroy()
            mycanvas9 = new Chart(document.getElementById("mycanvas9"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

        }

        const group2 = element.classList.contains("group2");
        if (group2 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[1];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[5];
            valueScoreMain.textContent = textContent;


            const group = document.querySelectorAll('.value-group-2');
            let newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })

            mycanvas2.destroy()
            mycanvas2 = new Chart(document.getElementById("mycanvas2"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

            mycanvas10.destroy()
            mycanvas10 = new Chart(document.getElementById("mycanvas10"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

        }

        const group3 = element.classList.contains("group3");
        if (group3 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[2];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[6];
            valueScoreMain.textContent = textContent;


            const group = document.querySelectorAll('.value-group-3');
            let newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })

            mycanvas3.destroy()
            mycanvas3 = new Chart(document.getElementById("mycanvas3"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

            mycanvas11.destroy()
            mycanvas11 = new Chart(document.getElementById("mycanvas11"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });
        }

        const group4 = element.classList.contains("group4");
        if (group4 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[3];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[7];
            valueScoreMain.textContent = textContent;


            const group = document.querySelectorAll('.value-group-4');
            let newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })

            mycanvas4.destroy()
            mycanvas4 = new Chart(document.getElementById("mycanvas4"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

            mycanvas12.destroy()
            mycanvas12 = new Chart(document.getElementById("mycanvas12"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });
        }

        const group5 = element.classList.contains("group5");
        if (group5 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[13];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[9];
            valueScoreMain.textContent = textContent;


            const group = document.querySelectorAll('.value-group-5');
            let newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })

            mycanvas5.destroy()
            mycanvas5 = new Chart(document.getElementById("mycanvas5"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

            mycanvas13.destroy()
            mycanvas13 = new Chart(document.getElementById("mycanvas13"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });
        }

        const group6 = element.classList.contains("group6");
        if (group6 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[14];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[10];
            valueScoreMain.textContent = textContent;



            const group = document.querySelectorAll('.value-group-6');
            let newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })

            mycanvas6.destroy()
            mycanvas6 = new Chart(document.getElementById("mycanvas6"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

            mycanvas14.destroy()
            mycanvas14 = new Chart(document.getElementById("mycanvas14"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });
        }

        const group7 = element.classList.contains("group7");
        if (group7 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[15];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[11];
            valueScoreMain.textContent = textContent;


            const group = document.querySelectorAll('.value-group-7');
            let newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })

            mycanvas7.destroy()
            mycanvas7 = new Chart(document.getElementById("mycanvas7"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

            mycanvas15.destroy()
            mycanvas15 = new Chart(document.getElementById("mycanvas15"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });
        }

        const group8 = element.classList.contains("group8");
        if (group8 && checkStatus) {

            const valueScore = document.querySelectorAll(".value-score")[16];
            const textContent = parseInt(valueScore.textContent) + 1;
            valueScore.textContent = textContent;

            const valueScoreMain = document.querySelectorAll(".value-score")[12];
            valueScoreMain.textContent = textContent;


            const group = document.querySelectorAll('.value-group-8');
            let newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })

            mycanvas8.destroy()
            mycanvas8 = new Chart(document.getElementById("mycanvas8"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });

            mycanvas16.destroy()
            mycanvas16 = new Chart(document.getElementById("mycanvas16"), {
                type: 'radar',
                data: {
                    labels: ['', '', '', '', '', '', '', ''],
                    datasets: [{
                        label: '',
                        data: newArray,
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

                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false, // Ẩn chú thích (legend)
                        },
                        datalabels: {
                            display: false, // Ẩn hiển thị dữ liệu trên biểu đồ
                        },
                    },
                    elements: {
                        line: {
                            borderWidth: 2,

                        },
                        point: {
                            radius: 2, // Đặt kích thước của hình tròn nhỏ hơn
                            borderWidth: 2, // Độ rộng của viền hình tròn
                        }
                    },
                    tooltips: {
                        enabled: false,
                    },
                }
            });
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