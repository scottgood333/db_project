function changeDistricts() {
    const county = document.getElementById("county").value;
    const districtSelect = document.getElementById("district");
    districtSelect.options.length = 0; // 清空行政區下拉選單
    
    // keelung 基隆
    if (county === "keelung") {
        const districts = ["信義區", "安樂區"];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // newtaipei 新北
    if (county === "newtaipei") {
        const districts = ['三峽區', '新店區', '八里區', '汐止區', '泰山區', '新莊區', '中和區', '三重區'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // taipei 臺北
    if (county === "taipei") {
        const districts = ['松山區', '北投區', '信義區', '大同區'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // taoyuan 桃園
    if (county === "taoyuan") {
        const districts = ['桃園區', '平鎮區', '龍潭區', '中壢區'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // hsinchu 新竹
    if (county === "hsinchu") {
        const districts = ['東區光', '竹北市', '北區金'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    
    // miaoli 苗栗
    if (county === "miaoli") {
        const districts = ['頭份市', '苗栗市'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }
    
    // taichung 臺中
    if (county === "taichung") {
        const districts = ['太平區', '豐原區', '西屯區', '大甲區', '中區平', '沙鹿區', '西區三', '梧棲區', '潭子區', '南屯區', '大里區'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }
    
    // changhua 彰化
    if (county === "changhua") {
        const districts = ['鹿港鎮', '埔心鄉', '彰化市'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // nantou 南投
    if (county === "nantou") {
        const districts = ['南投市', '草屯鎮', '埔里鎮'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }
    
    // yunlin 雲林
    if (county === "yunlin") {
        const districts = ['北港鎮', '斗六市'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // chiayi_county 嘉義縣
    if (county === "chiayi_county") {
        const districts = ['朴子市', '大林鎮'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // chiayi_city 嘉義市
    if (county === "chiayi_city") {
        const districts = ['東區', '西區'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // tainan 臺南
    if (county === "tainan") {
        const districts = ['東區泉', '仁德區', '麻豆區', '東區崇', '安南區', '柳營區', '中西區'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // kaohsiung 高雄
    if (county === "kaohsiung") {
        const districts = ['燕巢區', '苓雅區', '大寮區', '鼓山區', '前金區', '左營區', '小港區'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // yilan 宜蘭
    if (county === "yilan") {
        const districts = ['宜蘭市', '羅東鎮'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // hualien 花蓮
    if (county === "hualien") {
        const districts = ['花蓮市', '新城鄉'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }

    // taitung 臺東
    if (county === "taitung") {
        const districts = ['臺東市'];
        for (let i = 0; i < districts.length; i++) {
            const option = document.createElement("option");
            option.value = districts[i];
            option.text = districts[i];
            districtSelect.add(option);
        }
    }
}