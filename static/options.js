function updateOptions() {
    var countySelect = document.getElementById("county");
    var districtSelect = document.getElementById("district");
    // var departmentSelect = document.getElementById("department");

    // 清空行政區、診療科目下拉選單
    districtSelect.innerHTML = "";
    // departmentSelect.innerHTML = "";

    // 根據第一個選項的值，更新第二個選項的選項
    if (countySelect.value === "keelung") {
        // keelung 基隆
        var content = ["信義區", "安樂區"];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "基隆市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "newtaipei") {
        // newtaipei 新北市
        var content = ['三峽區', '新店區', '八里區', '汐止區', '泰山區', '新莊區', '中和區', '三重區'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "新北市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "taipei") {
        // taipei 臺北市
        var content = ['松山區', '北投區', '信義區', '大同區'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "臺北市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "taoyuan") {
        // taoyuan 桃園
        var content = ['桃園區', '平鎮區', '龍潭區', '中壢區'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "桃園市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "hsinchu") {
        // hsinchu 新竹市
        var content = ['東區光', '竹北市', '北區金'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "新竹市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "miaoli") {
        // miaoli 苗栗縣
        var content = ['頭份市', '苗栗市'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "苗栗縣" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "taichung") {
        // taichung 臺中市
        var content = ['太平區', '豐原區', '西屯區', '大甲區', '中區平', '沙鹿區', '西區三', '梧棲區', '潭子區', '南屯區', '大里區'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "臺中市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "changhua") {
        // changhua 彰化縣
        var content = ['鹿港鎮', '埔心鄉', '彰化市'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "彰化縣" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "nantou") {
        // nantou 南投縣
        var content = ['南投市', '草屯鎮', '埔里鎮'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "南投縣" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "yunlin") {
        // yunlin 雲林縣
        var content = ['北港鎮', '斗六市'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "雲林縣" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "chiayi_county") {
        // chiayi_county 嘉義縣
        var content = ['朴子市', '大林鎮'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "嘉義縣" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "chiayi_city") {
        // chiayi_city 嘉義市
        var content = ['東區', '西區'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "嘉義市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "tainan") {
        // tainan 臺南市
        var content = ['東區泉', '仁德區', '麻豆區', '東區崇', '安南區', '柳營區', '中西區'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "臺南市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "kaohsiung") {
        // kaohsiung 高雄市
        var content = ['燕巢區', '苓雅區', '大寮區', '鼓山區', '前金區', '左營區', '小港區'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "高雄市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "yilan") {
        // yilan 宜蘭縣
        var content = ['宜蘭市', '羅東鎮'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "宜蘭縣" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "hualien") {
        // hualien 花蓮市
        var content = ['花蓮市', '新城鄉'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "花蓮市" + content[i];
            districtSelect.add(option);
        }
    } else if (countySelect.value === "taitung") {
        // taitung 臺東市
        var content = ['臺東市'];
        for (let i = 0; i < content.length; i++) {
            var option = document.createElement("option");
            option.value = content[i];
            option.text = "臺東市" + content[i];
            districtSelect.add(option);
        }
    }

    
}