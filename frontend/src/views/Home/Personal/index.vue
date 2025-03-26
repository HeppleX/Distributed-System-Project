<template>
    <div class="personal" style="background-color: #ececec; padding: 20px">
        <a-row class="courseList" :gutter="16">
            <a-empty class="empty" v-if="!data.list.length" />
            <a-col v-else class="courseRow" :span="8" v-for="(item, index) in data.list">
                <a-card :title="item.course_name" :bordered="false">
                    <template #extra>
                        <a-button type="primary" danger @click="dropCourse(item.course_id)">Drop</a-button>
                    </template>
                    <p class="courseItem">
                        <a-tag color="pink">Course ID</a-tag>:
                        {{ item.course_id }}
                    </p>
                    <p>
                        <a-tag color="blue">Enroll Time</a-tag>:
                        {{ item.enroll_time }}
                    </p>
                </a-card>
            </a-col>
        </a-row>
    </div>
</template>

<script setup>
import { reactive } from 'vue';
import router from '@/router';
import { getAPI, postAPI } from '@/utils/api';
import { message } from 'ant-design-vue';
const data = reactive({
    list: []
});
function formatGMTString(gmtString) {
    const date = new Date(gmtString);

    const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0'); // 月份从 0 开始，需要 +1
    const day = String(date.getDate()).padStart(2, '0');
    const weekDay = daysOfWeek[date.getDay()];
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');

    return `${year}-${month}-${day} ${weekDay} ${hours}:${minutes}:${seconds}`;
}
const getData = async () => {
    await getAPI('/schedule').then(res => {
        if (res.status && res.status == 200) {
            data.list = res.data;
            if(data.list.length) {
                for (let i = 0; i < data.list.length; i++) {
                    data.list[i].enroll_time = formatGMTString(data.list[i].enroll_time);
                }
            }
        } else {
            message.info('There is something wrong!');
        }
    }).catch(err => {
        message.info('There is something wrong!');
    })
}
getData();
function dropCourse(ID) {
    postAPI("/drop", {
        course_id: ID
    }).then(res => {
        if (res.status && res.status == 200) {
            message.success('Drop success!');
            router.go(0);
        } else {
            message.info('There is something wrong!');
        }
    }).catch(err => {
        message.info('There is something wrong!');
    })
}
</script>

<style scoped>
.personal {
    overflow-y: auto;
    height: 100%;
}

.courseList {}

.courseRow {
    margin-bottom: 20px;
}

.courseItem {
    margin-bottom: 10px;
}

.empty {
    height: 100%;
    width: 100%;
}
</style>