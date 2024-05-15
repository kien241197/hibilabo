
function createChart(ctx, data, labels) {

  new Chart(ctx, {
    type: 'radar',
    data: {
      // ラベルも本当は動的にすべき
      labels: labels ? ['人に合わせられるタイプ', 'バランスタイプ', '感情を大切にするタイプ'] : ["", "", ""],
      datasets: [{
        label: '',
        // データも本当は動的にすべき
        data: data,
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
          max: 60,
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
          color: 'black',
          backdropColor: '#ffffff',
          backdropPadding: 5,
          padding: 20,
          },
      },
      },
  },
  });

}
function create_chart(id, data) {

  var strname = "mycanvas-" + id;

  //図を動的に生成
  var ctx = document.getElementById(strname);

  createChart(ctx, data, false)
}

function createChartSample() {

  var strname = "mycanvas-sample"
  var ctx = document.getElementById(strname);
  
  createChart(ctx, [6, 3, 7], true)
}