let charts = {};

function createChart(ctx, data, label) {

  if (charts[ctx]) {
            charts[ctx].destroy(); // Phá hủy biểu đồ cũ nếu có
        }

  charts[ctx] = new Chart(document.getElementById(ctx), {
    type: 'radar',
    data: {
      labels: label ? ['HP見える化', 'コンセプト・ヴィジョン', 'リーダー育成・　幹部育成', '面接・人生設計', '社内共有', '組織力', '評価制度', '個人チャート・自己分析'] : ['', '', '', '', '', '', '', ''],
      datasets: [{
        label: 'カルテット指数',
        data: data,
        // データライン
        borderColor: 'yellow',
        borderWidth: 4,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
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
          with: 500,
          height: 500,
          //メモリ線
          ticks: {
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
  });
}

function create_graph(id, data) {

  var strname = "mycanvas-" + id;
  createChart(strname, data, false)
}

function createGraphSample() {

  var strname = "mycanvas-sample"
  createChart(strname, [6, 3, 7, 5, 1, 2, 4, 6], true)
}
