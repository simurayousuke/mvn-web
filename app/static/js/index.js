layui.use(['layer', 'carousel'], function () {
    var layer = layui.layer;
    var carousel = layui.carousel;
    layer.msg('试试');

    const options = {
        elem: '#carousel'
        , width: '1060px'
        , arrow: 'hover'
        , height: '600px'
        , interval: 5000
    };

    if (document.body.clientHeight <= 768) {
        options.height = '450px';
    }
    var ins = carousel.render(options);
    window.onresize = function () {
        if (document.body.clientHeight <= 768) {
            options.height = '450px';
            ins.reload(options);
            NumPerYear.changeHeight(300);
            Protocol.changeHeight(300);
        } else {
            options.height = '600px';
            ins.reload(options);
            NumPerYear.changeHeight(500);
            Protocol.changeHeight(500);
        }
    };

});

const NumPerYearOptions = {
    container: 'num-per-year',
    width: 1000,
    height: 500
};

if (document.body.clientHeight <= 768) {
    NumPerYearOptions.height = 300;
}

const NumPerYear = new G2.Chart(NumPerYearOptions);

NumPerYear.source(statistics);
NumPerYear.scale('num', {
    min: 0
});

NumPerYear.scale('time', {
    range: [0, 1]
});

NumPerYear.tooltip({
    crosshairs: {
        type: 'line'
    }
});

NumPerYear.line().position('time*num');

NumPerYear.point().position('time*num').size(4).shape('circle').style({
    stroke: '#fff',
    lineWidth: 1
});

NumPerYear.render();

const ProtocolOptions = {
    container: 'protocol',
    width: 1000,
    height: 500
};

if (document.body.clientHeight <= 768) {
    ProtocolOptions.height = 300;
}

const Protocol = new G2.Chart(ProtocolOptions);
const DataView = DataSet.DataView;
const dv = new DataView();

dv.source(license).transform({
    type: 'percent',
    field: 'num',
    dimension: 'license',
    as: 'percent'
});

Protocol.source(dv, {
    percent: {
        formatter: function (num) {
            num = (num * 100) + '%';
            return num;
        }
    }
});
Protocol.coord('theta', {
    radius: 0.75
});

Protocol.tooltip({
    showTitle: false,
    itemTpl: '<li><span style="background-color:{color};" class="g2-tooltip-marker"></span>{name}: {value}</li>'
});

Protocol.intervalStack()
    .position('percent')
    .color('license')
    .label('percent', {
        formatter: function (num, license) {
            var percent = parseFloat(num).toFixed(2) + '%';
            return license.point.license + ': ' + percent;
        }
    })
    .tooltip('license*percent', function (license, percent) {
        percent = (percent * 100).toFixed(2) + '%';
        return {
            name: license,
            value: percent
        };
    })
    .style({
        lineWidth: 1,
        stroke: '#fff'
    });

Protocol.render();
