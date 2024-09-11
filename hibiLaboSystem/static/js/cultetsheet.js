$(document).ready(function () {

    const charts = {};

    Chart.register(ChartDataLabels);

    let size = null;
    let size1 = null;
    let size2 = null;
    if (window.innerWidth >= 3840) {
        size1 = 50;
        size2 = 50;
        size = 40;
    } else if (window.innerWidth >= 2880) {
        size1 = 35;
        size2 = 35;
        size = 30;
    } else if (window.innerWidth >= 2560) {
        size1 = 30;
        size2 = 30;
        size = 28;
    } else if (window.innerWidth >= 2400) {
        size1 = 30;
        size2 = 30;
        size = 26;
    } else if (window.innerWidth >= 2133) {
        size1 = 30;
        size2 = 30;
        size = 24;
    } else if (window.innerWidth >= 1920) {

        size = 20;
        size1 = 30;
        size2 = 30;

    } else if (window.innerWidth >= 1745) {
        size1 = 28;
        size2 = 28;
        size = 18;
    } else if (window.innerWidth >= 1536) {

        size1 = 24;
        size2 = 24;
        size = 16;
    } else if (window.innerWidth >= 1280) {
        size1 = 20;
        size2 = 20;
        size = 12;
    } else if (window.innerWidth >= 1097) {

        size = 12;
        size1 = 20;
        size2 = 22;
    } else if (window.innerWidth >= 960) {

        size = 10;
        size1 = 16;
        size2 = 16;
    } else if (window.innerWidth >= 768) {
        size = 8;
        size1 = 14;
        size2 = 14;
    } else if (window.innerWidth >= 350) {
        size = 16;
    }

    const pipChart1 = document.getElementById('pipChart1');
    var dataLabel = document.getElementById('data-label');
    const chart1 = new Chart(pipChart1, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [percent_start, 100 - percent_start],
                backgroundColor: ['#2CAEB5', '#EAA9CA'],
                borderWidth: 0,
                hoverOffset: 4
            }]
        },
        options: {
            datasets: {
                doughnut: {
                    cutout: '66%'
                }
            },
            events: ["mouseout", "touchstart", "touchmove", "touchend"],
            hover: {
                mode: 'nearest',
            },
            plugins: {
                datalabels: {
                    color: 'white',
                    display: true,
                    font: { size: size, weight: 700 },
                    offset: 0,
                    formatter: (value, context) => {
                        if (context.dataIndex === 0) {
                            return 'fan℃\n' + Number(value.toString()) + "%";
                        } else if (context.dataIndex === 1) {

                            // return 'fan℃\n   ' + value.toString();
                            return ''
                        }
                        return value.toString();
                    },
                },
            },
            legend: {
                display: false,
            },
            tooltips: {
                enabled: false,
            },

        },
    });


    const pipChart2 = document.getElementById('pipChart2');
    const chart2 = new Chart(pipChart2, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [percent_end, 100 - percent_end],
                backgroundColor: ['#2CAEB5', '#EAA9CA'],
                borderWidth: 0
            }]
        },
        options: {
            datasets: {
                doughnut: {
                    cutout: '66%'
                }
            },
            events: ["mouseout", "touchstart", "touchmove", "touchend"],
            plugins: {
                datalabels: {
                    color: 'white',
                    display: true,
                    font: { size: size, weight: 700 },
                    offset: 0,
                    formatter: (value, context) => {
                        if (context.dataIndex === 0) {
                            return 'fan℃\n   ' + Number(value.toString()) + "%";
                        } else if (context.dataIndex === 1) {
                            // return ' fan℃\n   ' + value.toString();
                            return ''
                        }
                        return value.toString();
                    },
                },
            },
            legend: {
                display: false,
            },
            tooltips: {
                enabled: false,
            },

        },

    });



    // 
    function doubleColumsBar(id, result) {

        
        if (charts[id]) {
            charts[id].destroy(); // Phá hủy biểu đồ cũ nếu có
        }

        let listLabel = result?.map(item => item.date) || []

        while(listLabel.length < 6){
            listLabel.push("")
        }

        

        charts[id] = new Chart(document.getElementById(id).getContext('2d'), {
            type: 'bar',
            data: {
                labels: listLabel,
                datasets: [{
                    label: '',
                    data: result?.map(item => item.total_logic_must) || [],
                    backgroundColor: '#2CAEB5',
                    borderWidth: 0
                },
                {
                    label: '',
                    data: result?.map(item => item.total_sense_want) || [],
                    backgroundColor: '#EAA9CA',
                    borderWidth: 0
                }
                ]
            },
            options: {
                // events: [],
                plugins: {
                    datalabels: {
                        text: {
                            display: true,
                            color: '#333',
                        },
                        color: "#ffffff",
                        font: { size: size2, weight: 700 },

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
                        }
                    },
                    y: {
                        grid: {
                            display: false
                        },
                        stacked: true,
                        ticks: {
                            color: '#000000',
                        }
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
    }

    doubleColumsBar('stackedChart2')

    // 
    // Biến để lưu trữ các biểu đồ theo ID của canvas

    // Cập nhật hàm oneColumBar
    function oneColumBar(id, labels, data, type) {
        // Kiểm tra xem biểu đồ với ID này đã tồn tại chưa
        if (charts[id]) {
            charts[id].destroy(); // Phá hủy biểu đồ cũ nếu có
        }
        
        let listLabel = labels

        while(listLabel.length < 6){
            listLabel.push("")
        }
        // Tạo biểu đồ mới
        charts[id] = new Chart(document.getElementById(id), {
            type: 'bar',
            data: {
                labels: listLabel,
                datasets: [{
                    label: '',
                    data: data,
                    backgroundColor: type === "TOTAL" ? "#2CAEB5" : '#C8C9CA',
                }]
            },
            options: {
                plugins: {


                    datalabels: {
                        anchor: 'end',
                        align: 'top',
                        offset: type === "TOTAL" ? -50 : -10,
                        color: type === "TOTAL" ? "#ffffff" : "#2CAEB5",
                        font: { size: size1 || 16, weight: 700 },
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
                        max: data?.length > 0  ? Math.max(...data) + 10 : 100,
                        min: 0,
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

        return charts[id];
    }

    oneColumBar('barChart1', [], [], "MANDARA and SELFCHECK and HONNE");
    oneColumBar('stackedChart1', [], [], "MANDARA and SELFCHECK and HONNE");
    oneColumBar('barChart2', [], [], "MANDARA and SELFCHECK and HONNE");
    oneColumBar('totalChart', ["2022/3", "2022/6", "2022/9", "2022/12", "2023/3", "2023/6", "2023/9", "2023/12", "2024/3", "2024/6", "2024/9", "2024/12", "2025/3", "2025/6"], [48, 53, 66, 78, 73, 70, 82, 73, 78, 66, 66, 70], "TOTAL");

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $("#buttonHonne").click(function () {

        const start_date = $('select[name="honne_start"]').val()
        const end_date = $('select[name="honne_end"]').val()
        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlHonne,
            data: {
                start_date,
                end_date,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {
                
                const labels = res.context.map(item =>  {

                    const date = new Date(item.date)
                    return `${date.getFullYear()}/${date.getMonth() + 1}`
                });

                const total = res.context.map(item => item.kartet_index_total);
                oneColumBar('stackedChart1', labels, total, "MANDARA and SELFCHECK and HONNE")
            }
        })
    })

    $("#buttonSelfCheck").click(function () {

        const start_date = $('select[name="selfcheck_start"]').val()
        const end_date = $('select[name="selfcheck_end"]').val()
        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlSelfCheck,
            data: {
                start_date,
                end_date,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {
                
                
                const labels = res.context.map(item =>  {

                    const date = new Date(item.date)
                    return `${date.getFullYear()}/${date.getMonth() + 1}`
                });

                const total = res.context.map(item => item.kartet_index_total);
                oneColumBar('barChart2', labels, total, "MANDARA and SELFCHECK and HONNE")
            }
        })
    })

    $("#buttonMandara").click(function () {

        const start_date = $('select[name="mandara_start"]').val()
        const end_date = $('select[name="mandara_end"]').val()
        const csrftoken = getCookie('csrftoken');
        
        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlMandara,
            data: {
                start_date,
                end_date,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                const labels = res.context.map(item =>  {

                    const date = new Date(item.date)
                    return `${date.getFullYear()}/${date.getMonth() + 1}`
                });

                const total = res.context.map(item => item?.total != 0 ? item.total  : "");
                oneColumBar('barChart1', labels, total, "MANDARA and SELFCHECK and HONNE")
            }
        })
    })

    $("#buttonBonknow").click(function () {

        const start_date = $('select[name="bonknow_start"]').val()
        const end_date = $('select[name="bonknow_end"]').val()
        const csrftoken = getCookie('csrftoken');
        
        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlBonknow,
            data: {
                start_date,
                end_date,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {
                
                const result  = res.context.context.map(item =>  {

                    const date = new Date(item.date)
                    return {
                        date: `${date.getFullYear()}/${date.getMonth() + 1}`,
                        total_logic_must: item.total_logic_must,
                        total_sense_want: item.total_sense_want
                    }
                });

               doubleColumsBar('stackedChart2', result)
            }
        })
    })

    $("#buttonFanTotal").click(function () {

        const start_date = $('select[name="total_start"]').val()
        const end_date = $('select[name="total_end"]').val()
        const csrftoken = getCookie('csrftoken');
        
        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlFanTotal,
            data: {
                start_date,
                end_date,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {
                
               
                console.log(res);
                
            }
        })
    })



    window.addEventListener('resize', () => {

        if (window.innerWidth <= 600) {
            chart1.options.plugins.datalabels.font.size = 12;
            chart2.options.plugins.datalabels.font.size = 12;
        }
        if (window.innerWidth >= 768) {

            chart1.options.plugins.datalabels.font.size = 8;
            chart2.options.plugins.datalabels.font.size = 8;
        }
        if (window.innerWidth >= 960) {

            chart1.options.plugins.datalabels.font.size = 10;
            chart2.options.plugins.datalabels.font.size = 10;
        }
        if (window.innerWidth >= 1097) {

            chart1.options.plugins.datalabels.font.size = 12;
            chart2.options.plugins.datalabels.font.size = 12;
        }
        if (window.innerWidth >= 1280) {
            chart1.options.plugins.datalabels.font.size = 12;
            chart2.options.plugins.datalabels.font.size = 12;
        }
        if (window.innerWidth >= 1536) {
            chart1.options.plugins.datalabels.font.size = 16;
            chart2.options.plugins.datalabels.font.size = 16;
        }
        if (window.innerWidth >= 1745) {
            chart1.options.plugins.datalabels.font.size = 18;
            chart2.options.plugins.datalabels.font.size = 18;
        }

        if (window.innerWidth >= 1920) {
            chart1.options.plugins.datalabels.font.size = 20;
            chart2.options.plugins.datalabels.font.size = 20;
        }

        if (window.innerWidth >= 2400) {
            chart1.options.plugins.datalabels.font.size = 22;
            chart2.options.plugins.datalabels.font.size = 22;
        }
        if (window.innerWidth >= 2133) {
            chart1.options.plugins.datalabels.font.size = 24;
            chart2.options.plugins.datalabels.font.size = 24;

        }

        if (window.innerWidth >= 2400) {
            chart1.options.plugins.datalabels.font.size = 26;
            chart2.options.plugins.datalabels.font.size = 26;
        }

        if (window.innerWidth >= 2560) {
            chart1.options.plugins.datalabels.font.size = 28;
            chart2.options.plugins.datalabels.font.size = 28;
        }
        if (window.innerWidth >= 2880) {
            chart1.options.plugins.datalabels.font.size = 30;
            chart2.options.plugins.datalabels.font.size = 30;
        }
        if (window.innerWidth >= 3840) {
            chart1.options.plugins.datalabels.font.size = 40;
            chart2.options.plugins.datalabels.font.size = 40;
        }
    });

})