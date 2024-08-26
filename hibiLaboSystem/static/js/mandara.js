$(document).ready(function () {

    const tab = $(".tab");
    const hash = window.location.hash;

    tab.css("display", "none");

    if (hash === "#mandara_personal" || !hash) {

        $(`#tab0`).css("display", "block");
        $('.mandara-nav').eq(0).addClass('active')
    }

    if (hash === "#mandara_masmas_chart") {

        $(`#tab1`).css("display", "block");
        $('.mandara-nav').eq(1).addClass('active')
        getMasMasMandaraAjax('', 1)
    }

    if (hash === "#mandara_completion_tab") {

        $(`#tab2`).css("display", "block");
        $('.mandara-nav').eq(2).addClass('active')
        getMandaraCompletionTabAjax()
    }

    $(".mandara-nav").click(function () {

        const index = $(this).closest("li").index();

        tab.css("display", "none");
        $(".mandara-nav").removeClass("active");


        $(`#tab${index}`).css("display", "block");
        $(this).addClass("active");


        if (index === 1) {
            const user_id = $('select[name="user_id"]').eq(1).val()
            getMasMasMandaraAjax(user_id, 1)
        }


        if (index === 2) {

            const user_id = $('select[name="user_id"]').eq(2).val()
            getMandaraCompletionTabAjax(user_id)
        }
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

        const user_id = $(this).find('select[name="user_id"]').val()
        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlMandaraPersonalAjax,
            data: {
                user_id,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {
                if (res.context.mandara) {
                    $('#mandaraPersonal').removeAttr('hidden');
                    var arrayChartGroupA = [res.context.mandara.A2_result, res.context.mandara.A3_result, res.context.mandara.A4_result, res.context.mandara.A5_result, res.context.mandara.A6_result, res.context.mandara.A7_result, res.context.mandara.A8_result, res.context.mandara.A1_result];
                    var arrayChartGroupB = [res.context.mandara.B2_result, res.context.mandara.B3_result, res.context.mandara.B4_result, res.context.mandara.B5_result, res.context.mandara.B6_result, res.context.mandara.B7_result, res.context.mandara.B8_result, res.context.mandara.B1_result];
                    var arrayChartGroupC = [res.context.mandara.C2_result, res.context.mandara.C3_result, res.context.mandara.C4_result, res.context.mandara.C5_result, res.context.mandara.C6_result, res.context.mandara.C7_result, res.context.mandara.C8_result, res.context.mandara.C1_result];
                    var arrayChartGroupH = [res.context.mandara.H2_result, res.context.mandara.H3_result, res.context.mandara.H4_result, res.context.mandara.H5_result, res.context.mandara.H6_result, res.context.mandara.H7_result, res.context.mandara.H8_result, res.context.mandara.H1_result];
                    var arrayChartGroupD = [res.context.mandara.D2_result, res.context.mandara.D3_result, res.context.mandara.D4_result, res.context.mandara.D5_result, res.context.mandara.D6_result, res.context.mandara.D7_result, res.context.mandara.D8_result, res.context.mandara.D1_result];
                    var arrayChartGroupG = [res.context.mandara.G2_result, res.context.mandara.G3_result, res.context.mandara.G4_result, res.context.mandara.G5_result, res.context.mandara.G6_result, res.context.mandara.G7_result, res.context.mandara.G8_result, res.context.mandara.G1_result];
                    var arrayChartGroupF = [res.context.mandara.F2_result, res.context.mandara.F3_result, res.context.mandara.F4_result, res.context.mandara.F5_result, res.context.mandara.F6_result, res.context.mandara.F7_result, res.context.mandara.F8_result, res.context.mandara.F1_result];
                    var arrayChartGroupE = [res.context.mandara.E2_result, res.context.mandara.E3_result, res.context.mandara.E4_result, res.context.mandara.E5_result, res.context.mandara.E6_result, res.context.mandara.E7_result, res.context.mandara.E8_result, res.context.mandara.E1_result];

                    var dataGroupF = [
                        [res.context.mandara.F1_result, res.context.mandara.F1_content],
                        [res.context.mandara.F2_result, res.context.mandara.F2_content],
                        [res.context.mandara.F3_result, res.context.mandara.F3_content],
                        [res.context.mandara.F8_result, res.context.mandara.F8_content],
                        [res.context.mandara.F4_result, res.context.mandara.F4_content],
                        [res.context.mandara.F7_result, res.context.mandara.F7_content],
                        [res.context.mandara.F6_result, res.context.mandara.F6_content],
                        [res.context.mandara.F5_result, res.context.mandara.F5_content]
                    ];
                    var groupF = $(".value-tableF");
                    groupF.each(function (index) {
                        var value = dataGroupF[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });

                    var dataGroupC = [
                        [res.context.mandara.C1_result, res.context.mandara.C1_content],
                        [res.context.mandara.C2_result, res.context.mandara.C2_content],
                        [res.context.mandara.C3_result, res.context.mandara.C3_content],
                        [res.context.mandara.C8_result, res.context.mandara.C8_content],
                        [res.context.mandara.C4_result, res.context.mandara.C4_content],
                        [res.context.mandara.C7_result, res.context.mandara.C7_content],
                        [res.context.mandara.C6_result, res.context.mandara.C6_content],
                        [res.context.mandara.C5_result, res.context.mandara.C5_content]
                    ];
                    var groupC = $(".value-tableC");
                    groupC.each(function (index) {
                        var value = dataGroupC[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });

                    var dataGroupG = [
                        [res.context.mandara.G1_result, res.context.mandara.G1_content],
                        [res.context.mandara.G2_result, res.context.mandara.G2_content],
                        [res.context.mandara.G3_result, res.context.mandara.G3_content],
                        [res.context.mandara.G8_result, res.context.mandara.G8_content],
                        [res.context.mandara.G4_result, res.context.mandara.G4_content],
                        [res.context.mandara.G7_result, res.context.mandara.G7_content],
                        [res.context.mandara.G6_result, res.context.mandara.G6_content],
                        [res.context.mandara.G5_result, res.context.mandara.G5_content]
                    ];

                    var groupG = $(".value-tableG");
                    groupG.each(function (index) {
                        var value = dataGroupG[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });
                    var dataGroupG = [
                        [res.context.mandara.G1_result, res.context.mandara.G1_content],
                        [res.context.mandara.G2_result, res.context.mandara.G2_content],
                        [res.context.mandara.G3_result, res.context.mandara.G3_content],
                        [res.context.mandara.G8_result, res.context.mandara.G8_content],
                        [res.context.mandara.G4_result, res.context.mandara.G4_content],
                        [res.context.mandara.G7_result, res.context.mandara.G7_content],
                        [res.context.mandara.G6_result, res.context.mandara.G6_content],
                        [res.context.mandara.G5_result, res.context.mandara.G5_content]
                    ];
                    var groupG = $(".value-tableG");
                    groupG.each(function (index) {
                        var value = dataGroupG[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });

                    var dataGroupB = [
                        [res.context.mandara.B1_result, res.context.mandara.B1_content],
                        [res.context.mandara.B2_result, res.context.mandara.B2_content],
                        [res.context.mandara.B3_result, res.context.mandara.B3_content],
                        [res.context.mandara.B8_result, res.context.mandara.B8_content],
                        [res.context.mandara.B4_result, res.context.mandara.B4_content],
                        [res.context.mandara.B7_result, res.context.mandara.B7_content],
                        [res.context.mandara.B6_result, res.context.mandara.B6_content],
                        [res.context.mandara.B5_result, res.context.mandara.B5_content]
                    ];
                    var groupB = $(".value-tableB");
                    groupB.each(function (index) {
                        var value = dataGroupB[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });

                    var dataGroupD = [
                        [res.context.mandara.D1_result, res.context.mandara.D1_content],
                        [res.context.mandara.D2_result, res.context.mandara.D2_content],
                        [res.context.mandara.D3_result, res.context.mandara.D3_content],
                        [res.context.mandara.D8_result, res.context.mandara.D8_content],
                        [res.context.mandara.D4_result, res.context.mandara.D4_content],
                        [res.context.mandara.D7_result, res.context.mandara.D7_content],
                        [res.context.mandara.D6_result, res.context.mandara.D6_content],
                        [res.context.mandara.D5_result, res.context.mandara.D5_content]
                    ];
                    var groupD = $(".value-tableD");
                    groupD.each(function (index) {
                        var value = dataGroupD[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });

                    var dataGroupE = [
                        [res.context.mandara.E1_result, res.context.mandara.E1_content],
                        [res.context.mandara.E2_result, res.context.mandara.E2_content],
                        [res.context.mandara.E3_result, res.context.mandara.E3_content],
                        [res.context.mandara.E8_result, res.context.mandara.E8_content],
                        [res.context.mandara.E4_result, res.context.mandara.E4_content],
                        [res.context.mandara.E7_result, res.context.mandara.E7_content],
                        [res.context.mandara.E6_result, res.context.mandara.E6_content],
                        [res.context.mandara.E5_result, res.context.mandara.E5_content]
                    ];
                    var groupE = $(".value-tableE");
                    groupE.each(function (index) {
                        var value = dataGroupE[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });

                    var dataGroupA = [
                        [res.context.mandara.A1_result, res.context.mandara.A1_content],
                        [res.context.mandara.A2_result, res.context.mandara.A2_content],
                        [res.context.mandara.A3_result, res.context.mandara.A3_content],
                        [res.context.mandara.A8_result, res.context.mandara.A8_content],
                        [res.context.mandara.A4_result, res.context.mandara.A4_content],
                        [res.context.mandara.A7_result, res.context.mandara.A7_content],
                        [res.context.mandara.A6_result, res.context.mandara.A6_content],
                        [res.context.mandara.A5_result, res.context.mandara.A5_content]
                    ];
                    var groupA = $(".value-tableA");
                    groupA.each(function (index) {

                        var value = dataGroupA[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });

                    var dataGroupH = [
                        [res.context.mandara.H1_result, res.context.mandara.H1_content],
                        [res.context.mandara.H2_result, res.context.mandara.H2_content],
                        [res.context.mandara.H3_result, res.context.mandara.H3_content],
                        [res.context.mandara.H8_result, res.context.mandara.H8_content],
                        [res.context.mandara.H4_result, res.context.mandara.H4_content],
                        [res.context.mandara.H7_result, res.context.mandara.H7_content],
                        [res.context.mandara.H6_result, res.context.mandara.H6_content],
                        [res.context.mandara.H5_result, res.context.mandara.H5_content]
                    ];
                    var groupH = $(".value-tableH");
                    groupH.each(function (index) {
                        var value = dataGroupH[index];

                        $(this).find("span").text(value[0]);
                        $(this).find("p").text(value[1]);
                    });

                    const result = ["A", "B", "C", "D", "E", "F", "G", "H"]
                    const valueResult = [
                        res.context.mandara.A_result,
                        res.context.mandara.B_result,
                        res.context.mandara.C_result,
                        res.context.mandara.D_result,
                        res.context.mandara.E_result,
                        res.context.mandara.F_result,
                        res.context.mandara.G_result,
                        res.context.mandara.H_result
                    ]
                    valueResult.map((item, index) => {

                        $(`.value-score${result[index]}`).text(item)

                    })

                    const titleMainSocre = [
                        res.context.mandara.A_dueto,
                        res.context.mandara.B_dueto,
                        res.context.mandara.C_dueto,
                        res.context.mandara.D_dueto,
                        res.context.mandara.E_dueto,
                        res.context.mandara.F_dueto,
                        res.context.mandara.G_dueto,
                        res.context.mandara.H_dueto
                    ]

                    titleMainSocre.map((item, index) => {

                        $(`.title-main-score${result[index]}`).text(item)
                    })

                    const totalValueResult = valueResult.reduce((acc, val) => acc + val, 0)
                    $('.value-score-center').text(totalValueResult)

                    function setCanvas(id, values) {
                        if (document.getElementById(id)) {
                            new Chart(document.getElementById(id), {
                                type: 'radar',
                                data: {
                                    labels: ['', '', '', '', '', '', '', ''],
                                    datasets: [{
                                        label: '',
                                        data: values,
                                        fill: true,
                                        borderColor: "#e9e2a0",
                                        pointBackgroundColor: '#e2db9d',
                                    }]
                                },
                                options: {
                                    tooltips: false,
                                    legend: {
                                        display: false
                                    },
                                    scale: {
                                        gridLines: {
                                            circular: false,
                                            color: "gray"
                                        },
                                        ticks: {
                                            display: false
                                        }
                                    },
                                },

                            });
                        }
                    }

                    setCanvas("mycanvasA", arrayChartGroupA);
                    setCanvas("mycanvasB", arrayChartGroupB);
                    setCanvas("mycanvasC", arrayChartGroupC);
                    setCanvas("mycanvasH", arrayChartGroupH);
                    setCanvas("mycanvasD", arrayChartGroupD);
                    setCanvas("mycanvasE", arrayChartGroupE);
                    setCanvas("mycanvasF", arrayChartGroupF);
                    setCanvas("mycanvasG", arrayChartGroupG);
                } else {
                    $('#mandaraPersonal').attr('hidden', true);
                }
            },
            error: function (error) {

                console.log(error);
            }
        })
    });

    function getMasMasMandaraAjax(user_id, type) {

        $.ajax({
            type: "GET",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlMasMasMandaraChartAjax,
            data: {
                user_id
            },
            success: function (res) {
                if (res?.context) {

                    $('label[name="start"]').eq(0).text(res.context.start);
                    $('label[name="end"]').eq(0).text(res.context.end);

                    if (type !== 1) {
                        const barChart1 = document.getElementById('barChart').getContext('2d');
                        new Chart(barChart1, {
                            type: 'bar',
                            data: {
                                labels: res.context.list_month.length >= 5 ? res.context.list_month : [...res.context.list_month, "", "", "", "", "", ""],
                                datasets: [{
                                    label: '', // Bỏ label
                                    data: res.context.list_value,
                                    backgroundColor: '#C8C9CA',
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

                                },
                                legend: {
                                    display: false
                                },
                                scales: {
                                    xAxes: [{
                                        gridLines: {
                                            drawOnChartArea: false
                                        }
                                    }],
                                    yAxes: [{
                                        gridLines: {
                                            drawOnChartArea: false
                                        }
                                    }]
                                }
                            },
                        });
                    }
                }

            },
            error: function (error) {

                console.log(error);
            }
        })
    }

    $("#myForm1").submit(function (event) {

        event.preventDefault()
        const user_id = $(this).find('select[name="user_id"]').val()

        getMasMasMandaraAjax(user_id, 0);
    })

    function getMandaraCompletionTabAjax(user_id) {


        $.ajax({
            type: "GET",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlMandaraCompletionTabAjax,
            data: {
                user_id
            },
            success: function (res) {

                if (res?.context?.start && res?.context?.end) {
                    $('label[name="start"]').eq(1).text(res.context.start);
                    $('label[name="end"]').eq(1).text(res.context.end);
                }

                if (res?.context?.mandaras && res?.context?.mandaras?.length > 0) {

                    let html = ''
                    res.context.mandaras.forEach(element => {
                        html = `
                        <a href="/mandara-completion-tab-detail/${element.id}">
                            <div class="wrapper-date">
                                <div
                                    class="desc-item d-flex justify-content-center align-items-center">
                                    <div class="mr-2">
                                        <b>${res.context.start} ～ ${res.context.end}</b>
                                    </div>
                                    <svg fill="black" xmlns="http://www.w3.org/2000/svg" width="30"
                                        height="30" class="bi bi-caret-right" viewBox="0 0 16 16">
                                        <path
                                            d="M6 12.796V3.204L11.481 8 6 12.796zm.659.753 5.48-4.796a1 1 0 0 0 0-1.506L6.66 2.451C6.011 1.885 5 2.345 5 3.204v9.592a1 1 0 0 0 1.659.753z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                        </a>`
                    });

                    $('.item-date').html(html)
                } else {

                    $('.item-date').html('')

                }



            },
            error: function (error) {

                console.log(error);
            }
        })
    }

    $('#myForm2').submit(function (event) {

        event.preventDefault();
        const user_id = $(this).find('select[name="user_id"]').val()
        getMandaraCompletionTabAjax(user_id)
    })
})