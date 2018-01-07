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

const NumPerYearData = [
    {year: '1991', value: 3},
    {year: '1992', value: 4},
    {year: '1993', value: 3.5},
    {year: '1994', value: 5},
    {year: '1995', value: 4.9},
    {year: '1996', value: 6},
    {year: '1997', value: 7},
    {year: '1998', value: 9},
    {year: '1999', value: 13}
];

const NumPerYearOptions = {
    container: 'num-per-year',
    width: 1000,
    height: 500
};
if (document.body.clientHeight <= 768) {
    NumPerYearOptions.height = 300;
}

const NumPerYear = new G2.Chart(NumPerYearOptions);

NumPerYear.source(NumPerYearData);
NumPerYear.scale('value', {
    min: 0
});
NumPerYear.scale('year', {
    range: [0, 1]
});
NumPerYear.tooltip({
    crosshairs: {
        type: 'line'
    }
});
NumPerYear.line().position('year*value');
NumPerYear.point().position('year*value').size(4).shape('circle').style({
    stroke: '#fff',
    lineWidth: 1
});
NumPerYear.render();

const ProtocolData = [
    {year: '2001', population: 41.8},
    {year: '2002', population: 38},
    {year: '2003', population: 33.7},
    {year: '2004', population: 30.7},
    {year: '2005', population: 25.8},
    {year: '2006', population: 31.7},
    {year: '2007', population: 33},
    {year: '2008', population: 46},
    {year: '2009', population: 38.3},
    {year: '2010', population: 28},
    {year: '2011', population: 42.5},
    {year: '2012', population: 30.3}
];

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
dv.source(data).transform({
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
// Protocol.legend({
//     position: 'right',
//     offsetY: -40,
//     offsetX: -200
// });

Protocol.tooltip({
    showTitle: false,
    itemTpl: '<li><span style="background-color:{color};" class="g2-tooltip-marker"></span>{name}: {value}</li>'
});

// Protocol.axis(false);
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



