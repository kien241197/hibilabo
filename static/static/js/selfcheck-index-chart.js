function create_chart(id, data) {
    var strname = "mycanvas-" + id;

    //図を動的に生成
    var ctx = document.getElementById(strname);
    var myChart = new Chart(ctx, {
      type: 'radar',
      data: {
        labels: ['', '', '', '', '','', '', '', '','', '', ''],
        datasets: [{
          label: '',
          data: data,
          // データライン
          borderColor: 'yellow',
          borderWidth: 4,
        }],
      },
      options: {
        scales: {
          r: {
            // 最小値・最大値
            min: 0,
            max: 15,
            //メモリ線
            ticks:{
              display: false
            },
            // 背景色
            backgroundColor: 'darkgray',
            // グリッドライン
            grid: {
              color: 'gainsboro',
            },
            // アングルライン
            angleLines: {
              color: 'darkgray',
            },
            // ポイントラベル
            pointLabels: {
              display: false,
            },
          },
        },
        plugins: {
            legend: {
              display: false
            }
        },

      },
    });

}