Chart.register(ChartDataLabels);

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


var mycanvas1 = new Chart(document.getElementById("mycanvas1"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: [arrayGroup1[1], arrayGroup1[2], arrayGroup1[4], arrayGroup1[7], arrayGroup1[6], arrayGroup1[5], arrayGroup1[3], arrayGroup1[0]],
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

                min: 0
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
        r: {

            //メモリ線
            ticks: {
                display: false
            },
        }
    }
});

var mycanvas2 = new Chart(document.getElementById("mycanvas2"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: [arrayGroup2[1], arrayGroup2[2], arrayGroup2[4], arrayGroup2[7], arrayGroup2[6], arrayGroup2[5], arrayGroup2[3], arrayGroup2[0]],
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
                min: 0
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
            data: [arrayGroup3[1], arrayGroup3[2], arrayGroup3[4], arrayGroup3[7], arrayGroup3[6], arrayGroup3[5], arrayGroup3[3], arrayGroup3[0]],
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
                },
                min: 0
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
            data: [arrayGroup4[1], arrayGroup4[2], arrayGroup4[4], arrayGroup4[7], arrayGroup4[6], arrayGroup4[5], arrayGroup4[3], arrayGroup4[0]],
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
                },
                min: 0
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
            data: [arrayGroup5[1], arrayGroup5[2], arrayGroup5[4], arrayGroup5[7], arrayGroup5[6], arrayGroup5[5], arrayGroup5[3], arrayGroup5[0]],
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
                },
                min: 0
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
            data: [arrayGroup6[1], arrayGroup6[2], arrayGroup6[4], arrayGroup6[7], arrayGroup6[6], arrayGroup6[5], arrayGroup6[3], arrayGroup6[0]],
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
                },
                min: 0,
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
            data: [arrayGroup7[1], arrayGroup7[2], arrayGroup7[4], arrayGroup7[7], arrayGroup7[6], arrayGroup7[5], arrayGroup7[3], arrayGroup7[0]],
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
                },
                min: 0
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
            data: [arrayGroup8[1], arrayGroup8[2], arrayGroup8[4], arrayGroup8[7], arrayGroup8[6], arrayGroup8[5], arrayGroup8[3], arrayGroup8[0]],
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
                },
                min: 0
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
            // data: [1,2,3,4,5,6,7,8],
            data: [arrayGroup1[1], arrayGroup1[2], arrayGroup1[4], arrayGroup1[7], arrayGroup1[6], arrayGroup1[5], arrayGroup1[3], arrayGroup1[0]],

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

                },
                min: 0
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
            data: [arrayGroup2[1], arrayGroup2[2], arrayGroup2[4], arrayGroup2[7], arrayGroup2[6], arrayGroup2[5], arrayGroup2[3], arrayGroup2[0]],
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
                },
                min: 0
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
            data: [arrayGroup3[1], arrayGroup3[2], arrayGroup3[4], arrayGroup3[7], arrayGroup3[6], arrayGroup3[5], arrayGroup3[3], arrayGroup3[0]],
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
                },
                min: 0
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
            data: [arrayGroup4[1], arrayGroup4[2], arrayGroup4[4], arrayGroup4[7], arrayGroup4[6], arrayGroup4[5], arrayGroup4[3], arrayGroup4[0]],
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
                },
                min: 0
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
            data: [arrayGroup5[1], arrayGroup5[2], arrayGroup5[4], arrayGroup5[7], arrayGroup5[6], arrayGroup5[5], arrayGroup5[3], arrayGroup5[0]],
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
                },
                min: 0
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
            data: [arrayGroup6[1], arrayGroup6[2], arrayGroup6[4], arrayGroup6[7], arrayGroup6[6], arrayGroup6[5], arrayGroup6[3], arrayGroup6[0]],
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

                },
                min: 0
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

var mycanvas15 = new Chart(document.getElementById("mycanvas15"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: [arrayGroup7[1], arrayGroup7[2], arrayGroup7[4], arrayGroup7[7], arrayGroup7[6], arrayGroup7[5], arrayGroup7[3], arrayGroup7[0]],
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

                },
                min: 0
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

var mycanvas16 = new Chart(document.getElementById("mycanvas16"), {
    type: 'radar',
    data: {
        labels: ['', '', '', '', '', '', '', ''],
        datasets: [{
            label: '',
            data: [arrayGroup8[1], arrayGroup8[2], arrayGroup8[4], arrayGroup8[7], arrayGroup8[6], arrayGroup8[5], arrayGroup8[3], arrayGroup8[0]],
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

                },
                min: 0
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
            var newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })
            newArray = [newArray[1], newArray[2], newArray[4], newArray[7], newArray[6], newArray[5], newArray[3], newArray[0]]
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
                            },
                            min: 0
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
                            },
                            min: 0
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
            var newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })
            newArray = [newArray[1], newArray[2], newArray[4], newArray[7], newArray[6], newArray[5], newArray[3], newArray[0]]
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

                            },
                            min: 0
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

                            },
                            min: 0
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
            var newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })
            newArray = [newArray[1], newArray[2], newArray[4], newArray[7], newArray[6], newArray[5], newArray[3], newArray[0]]
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

                            },
                            min: 0
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
                            },
                            min: 0
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
            var newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })
            newArray = [newArray[1], newArray[2], newArray[4], newArray[7], newArray[6], newArray[5], newArray[3], newArray[0]]
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
                            },
                            min: 0
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
                            },
                            min: 0
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
            var newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })
            newArray = [newArray[1], newArray[2], newArray[4], newArray[7], newArray[6], newArray[5], newArray[3], newArray[0]]
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
                            },
                            min: 0
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
                            },
                            min: 0
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
            var newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })
            newArray = [newArray[1], newArray[2], newArray[4], newArray[7], newArray[6], newArray[5], newArray[3], newArray[0]]
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
                            },
                            min: 0
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
                            },
                            min: 0
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
            var newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })
            newArray = [newArray[1], newArray[2], newArray[4], newArray[7], newArray[6], newArray[5], newArray[3], newArray[0]]
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
                            },
                            min: 0
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
                            },
                            min: 0
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
            var newArray = [];
            group.forEach(item => {

                newArray.push(item.textContent);
            })
            newArray = [newArray[1], newArray[2], newArray[4], newArray[7], newArray[6], newArray[5], newArray[3], newArray[0]]
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
                            },
                            min: 0
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
                            },
                            min: 0
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

// cũ