    //〇の数をカウントして、合計行を修正
    function func_count(element, listQ){
        counter_group = [0,0,0,0,0,0,0,0];
        listQ.forEach(key => {
            let value = $('#result'+key).val();
            let arr_index = $('#result'+key).closest('td').find('#index-'+key).val().split(',');
            for (var i = 0; i < 8; i++) {
                if(value == '1' && arr_index[i] == 'True') {
                    counter_group[i] += 1;
                }
            }
        })
        drwa_chart(counter_group);
    }

function drwa_chart(chatValue){
    var ctx = document.getElementById('mycanvas');
    //前のチャートがあったら消す
    if (myChart){
        console.log("OK");
        myChart.destroy();
    }else{
        console.log("NG");
    }

    myChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['HP見える化', 'コンセプト・ヴィジョン', 'リーダー育成・　幹部育成', '面接・人生設計', '社内共有','組織力','評価制度','個人チャート・自己分析'],
            datasets: [{
            label: 'カルテット指数',
            //data: [10, 16, 13, 12, 16, 15, 14, 17],
            data: [chatValue[0], chatValue[1], chatValue[2], chatValue[3], chatValue[4], chatValue[5], chatValue[6], chatValue[7]],
            // データライン
            borderColor: 'yellow',
            borderWidth: 4,

            }],
        },
        options: {
            //タイトル消
            plugins: {
　　                legend: {
               display: false
               },
               //https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#anchoring
               datalabels: {
                    font: {
                    size: 20
                    },
                },
            },
            scales: {
            r: {
                //メモリ線
                ticks:{
                    display: false
                },
                // 最小値・最大値
                min: 0,
                max: 10,
                // 背景色
                backgroundColor: 'darkgray',
                // グリッドライン
                grid: {
                color: 'gainsboro',
                borderWidth: 4,
                },
                // アングルライン
                angleLines: {
                color: 'darkgray',
                },
                // ポイントラベル
                pointLabels: {
                    color: 'black',
                    backdropColor: '#ffffff',
                    font: 10,

                },
            },
            },
        },
        plugins: [ChartDataLabels],
    });
}