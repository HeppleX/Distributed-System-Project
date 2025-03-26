<template>
    <div class="list" style="background-color: #ececec; padding: 20px">
        <a-row class="courseList" :gutter="16">
            <a-col class="courseRow" :span="8" v-for="(item, index) in data.list">
                <a-card :title="item.course_name" :bordered="false">
                    <template #extra>
                        <a-button
                            type="primary"
                            @click="enrollCourse(item.course_id)"
                            :disabled="(item.current_enrollment >= item.total_seats) || getDaysDifference(item.start_time, item.end_time) >= 100"
                        >Enroll</a-button>
                    </template>
                    <div class="courseCard">
                        <div>
                            <p class="courseItem">
                                <a-tag color="pink">Course ID</a-tag>:
                                {{ item.course_id }}
                            </p>
                            <p class="courseItem">
                                <a-tag color="orange">Total Seats</a-tag>:
                                {{ item.total_seats }}
                            </p>
                            <p class="courseItem">
                                <a-tag color="green">Current Enrollment</a-tag>:
                                {{ item.current_enrollment }}
                            </p>
                            <p class="courseItem">
                                <a-tag color="cyan">Start Time</a-tag>:
                                {{ item.start_time }}
                            </p>
                            <p>
                                <a-tag color="blue">End Time</a-tag>:
                                {{ item.end_time }}
                            </p>
                        </div>
                        <div>
                            <a-progress
                                class="plot"
                                type="circle"
                                :percent="Math.ceil(item.current_enrollment * 100 / item.total_seats)"
                            >
                            </a-progress>
                            <a-progress
                                class="progress"
                                :percent="getDaysDifference(item.start_time, item.end_time)"
                            />
                        </div>
                    </div>
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
const getDaysDifference = (startTime, endTime) => {
    const now = new Date();
    const endDate = new Date(endTime);
    const startDate = new Date(startTime);
    const period = endDate - startDate;
    const timeDiff = now - startDate;
    
    return Math.ceil(timeDiff * 100 / period);
}
const getData = async () => {
    await getAPI('/courses').then(res => {
        if (res.status && res.status == 200) {
            data.list = res.data.courses;
        } else {
            message.info('There is something wrong!');
        }
    }).catch(err => {
        message.info('There is something wrong!');
    })
}
getData();
function enrollCourse(ID) {
    postAPI("/enroll", {
        course_id: ID
    }).then(res => {
        if (res.status && res.status == 200) {
            message.success('Enroll success!');
        } else {
            if(res.data.message) {
                message.info(res.data.message);
            }else {
                message.info('There is something wrong!');
            }
        }
    }).catch(err => {
        message.info('There is something wrong!');
    })
}
</script>

<style scoped>
.list {
    overflow-y: auto;
    height: 100%;
}

.courseList {
}

.courseRow {
    margin-bottom: 20px;
}

.courseItem {
    margin-bottom: 10px;
}

.courseCard {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.plot {
    margin-top: -10px;
    margin-right: 50px;
    margin-bottom: 10px;
}

.progress {
    margin-left: -50px;
}
</style>