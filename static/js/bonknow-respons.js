Chart.register(ChartDataLabels);

const mycanvas = document.getElementById('mycanvas').getContext('2d');
const chart = new Chart(mycanvas, {
    type: 'bar',
    data: {
        labels: time_list.length >= 5 ? time_list : [...time_list, "", ""],
        datasets: [
            {
                label: 'Sense',
                data: sense_list,
                backgroundColor: '#2CAEB5',
                borderWidth: 0
            },
            {
                label: 'Logic',
                data: logic_list,
                backgroundColor: '#EAA9CA',
                borderWidth: 0
            }
        ]
    },
    options: {
        barThickness: 100,
        // events: [],
        plugins: {
            datalabels: {
                text: {
                    display: true,
                    color: '#333',
                },
                color: "#ffffff",
                font: { size: window.innerWidth <= 500 ? 20 : 30, weight: 700 },

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
                stacked: true,
                ticks: {
                    color: '#000000',
                    font: { size: window.innerWidth <= 500 ? 12 : 20 }
                }
            },
            y: {
                grid: {
                    display: false
                },
                stacked: true,
                ticks: {
                    color: '#000000',
                    font: { size: window.innerWidth <= 500 ? 12 : 20 },
                    stepSize: 20
                },
                min: 0,
                max: 100,
            }
        },
        elements: {
            bar: {
                barPercentage: 1,
                categoryPercentage: 1,
            }
        },
        hover: {
            mode: 'nearest',
        },

    },
});

window.addEventListener('resize', () => {

    if (window.innerWidth <= 500) {
        chart.options.scales.x.ticks.font.size = 12;
        chart.options.scales.y.ticks.font.size = 12;
        chart.options.plugins.datalabels.font.size = 20;
    } else {
        chart.options.scales.x.ticks.font.size = 20;
        chart.options.scales.y.ticks.font.size = 20;
        chart.options.plugins.datalabels.font.size = 30;
    }
})

