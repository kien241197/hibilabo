Chart.register(ChartDataLabels);
var chart, chart2;
function func_count_res(element, listQ){
    let logic = 0;
    let sense = 0;
    counter_group = [0,0];
    listQ.forEach(key => {
        let value = $('#respons_result'+key).val();
        let arr_index = $('#respons_result'+key).closest('td').find('#respons-type-'+key).val();
        if((value == '1' && arr_index == '1') || (arr_index == '2' && value == '0')) {
            logic += 1;
        }
        if((value == '1' && arr_index == '2') || (arr_index == '1' && value == '0')) {
            sense += 1;
        }
    })
    counter_group[1] = Math.round(logic / listQ.length * 100 * 100) / 100;
    counter_group[0] = Math.round(sense / listQ.length * 100 * 100) / 100;
    drwa_chart_res(counter_group);
}

function drwa_chart_res(chartValue){
    $('#sense').val(chartValue[0]);
    $('#logic').val(chartValue[1]);
    if (chart){
        chart.destroy();
    }
    var mycanvas = document.getElementById('mycanvas');
    chart = new Chart(mycanvas, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: chartValue,
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
                    font: { size: window.innerWidth <= 1097 ? 13 : 20, weight: 700 },
                    offset: 0,
                    formatter: (value, context) => {
                        if (context.dataIndex == 0) {
                            if(value != 0){

                                return 'SENSE\n   ' + value.toString() + "%";
                            } else {
                                return null;
                            }
                        } else if (context.dataIndex === 1) {
                            if(value != 0){

                                return ' LOGIC\n   ' + value.toString() + "%";
                            } else{
                                return null;
                            }
                           
                        }
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
}

function func_count_think(element, listQ){
    let must = 0, want = 0;
    counter_group = [0,0];
    listQ.forEach(key => {
        let value = $('#think_result'+key).val();
        let arr_index = $('#think_result'+key).closest('td').find('#think-type-'+key).val();
        if((value == '1' && arr_index == '1') || (arr_index == '2' && value == '0')) {
            must += 1;
        }
        if((value == '1' && arr_index == '2') || (arr_index == '1' && value == '0')) {
            want += 1;
        }
    })
    counter_group[1] = Math.round(must / listQ.length * 100 * 100) / 100;
    counter_group[0] = Math.round(want / listQ.length * 100 * 100) / 100;
    drwa_chart_think(counter_group);
}

function drwa_chart_think(chartValue){
    $('#must').val(chartValue[1]);
    $('#want').val(chartValue[0]);
    if (chart2){
        chart2.destroy();
    }
    var mycanvas2 = document.getElementById('mycanvas2');
    chart2 = new Chart(mycanvas2, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: chartValue,
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
                    font: { size: window.innerWidth <= 1097 ? 13 : 20, weight: 700 },
                    offset: 0,
                    formatter: (value, context) => {
                        if (context.dataIndex == 0) {
                            if(value != 0){

                                return 'WANT\n  ' + value.toString() + "%";
                            } else {

                                return null;
                            }
                        } else if (context.dataIndex === 1) {
                            if(value != 0){

                                return 'MUST\n  ' + value.toString() + "%";
                            } else{

                                return null;
                            }
                            
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
}

window.addEventListener('resize', () => {

    if (window.innerWidth <= 1097) {
        chart.options.plugins.datalabels.font.size = 13;
        chart2.options.plugins.datalabels.font.size = 13;
    } else {
        chart.options.plugins.datalabels.font.size = 20;
        chart2.options.plugins.datalabels.font.size = 20;
    }
})

document.addEventListener("DOMContentLoaded", function(event) { 
    var logic_first = 0, sense_first = 0, must_first = 0, want_first = 0;
    var respons_first = [0,0], think_first = [0,0];
    if(resList.length > 0) {
        resList.forEach(key => {
            let value = $('#respons_result'+key).val();
            let arr_index = $('#respons_result'+key).closest('td').find('#respons-type-'+key).val();
            if((value == '1' && arr_index == '1') || (arr_index == '2' && value == '0')) {
                logic_first += 1;
            }
            if((value == '1' && arr_index == '2') || (arr_index == '1' && value == '0')) {
                sense_first += 1;
            }
        })
        respons_first[1] = Math.round(logic_first / resList.length * 100 * 100) / 100;
        respons_first[0] = Math.round(sense_first / resList.length * 100 * 100) / 100;    
    }
    if(thinkList.length > 0) {
        thinkList.forEach(key => {
            let value = $('#think_result'+key).val();
            let arr_index = $('#think_result'+key).closest('td').find('#think-type-'+key).val();
            if((value == '1' && arr_index == '1') || (arr_index == '2' && value == '0')) {
                must_first += 1;
            }
            if((value == '1' && arr_index == '2') || (arr_index == '1' && value == '0')) {
                want_first += 1;
            }
        })
        think_first[1] = Math.round(must_first / thinkList.length * 100 * 100) / 100;
        think_first[0] = Math.round(want_first / thinkList.length * 100 * 100) / 100;    
    }
    drwa_chart_res(respons_first);

    drwa_chart_think(think_first);
});