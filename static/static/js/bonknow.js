$(document).ready(function () {

    const tab = $(".tab");
    const hash = window.location.hash;

    tab.css("display", "none");

    if (hash === "#bonknow_think" || !hash) {

        $(`#tab0`).css("display", "block");
        $('.bonknow-nav').eq(0).addClass('active')
    }

    if (hash === "#bonknow_response") {

        $(`#tab1`).css("display", "block");
        $('.bonknow-nav').eq(1).addClass('active')
    }

    $(".bonknow-nav").click(function () {

        const index = $(this).closest("li").index();

        tab.css("display", "none");
        $(".bonknow-nav").removeClass("active");


        $(`#tab${index}`).css("display", "block");
        $(this).addClass("active");
    })

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

    $("#myForm").submit(function (event) {

        event.preventDefault();

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlBonknowThinkAjax,
            data: {
                evaluation_unit,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                Chart.register(ChartDataLabels);

                const time_list = res.context.times
                const want_list = res.context.want
                const must_list = res.context.must

                const mycanvas = document.getElementById('mycanvas').getContext('2d');
                new Chart(mycanvas, {
                    type: 'bar',
                    data: {
                        labels: time_list.length >= 5 ? time_list : [...time_list, "", ""],
                        datasets: [
                            {
                                label: 'Want',
                                data: want_list,
                                backgroundColor: '#2CAEB5',
                                borderWidth: 0,
                            },
                            {
                                label: 'Must',
                                data: must_list,
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
                                    barThickness: 100
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

            },
            error: function (error) {

                console.log(error);
            }
        })
    });

    $("#myForm1").submit(function (event) {

        event.preventDefault();


        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlBonknowResponsAjax,
            data: {
                evaluation_unit,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {


                const time_list = res.context.times
                const sense_list = res.context.sense
                const logic_list = res.context.logic

                Chart.register(ChartDataLabels);

                const mycanvas = document.getElementById('mycanvas1').getContext('2d');
                new Chart(mycanvas, {
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


            },
            error: function (error) {

                console.log(error);
            }
        })
    });
})