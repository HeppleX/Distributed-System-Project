<template>
    <a-layout id="components-layout-demo-custom-trigger">
        <a-layout-sider v-model:collapsed="collapsed" :trigger="null" collapsible>
            <div class="logo">
                <template v-if="title">
                    {{ collapsed? "Course": title }}
                </template>
                <template v-else>
                    {{ collapsed? "Course": "Course Selection" }}
                </template>
            </div>
            <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
                <router-link to="/home/personal" custom v-slot="{ navigate }">
                    <a-menu-item key="/home/personal" @click="navigate" @keypress.enter="navigate" role="link">
                        <UserOutlined />
                        <span>Personal</span>
                    </a-menu-item>
                </router-link>
                <router-link to="/home/list" custom v-slot="{ navigate }">
                    <a-menu-item key="/home/list" @click="navigate" @keypress.enter="navigate" role="link">
                        <UnorderedListOutlined />
                        <span>List</span>
                    </a-menu-item>
                </router-link>
            </a-menu>
        </a-layout-sider>
        <a-layout>
            <a-layout-header style="background: #fff; padding: 0">
                <menu-unfold-outlined v-if="collapsed" class="trigger" @click="() => (collapsed = !collapsed)" />
                <menu-fold-outlined v-else class="trigger" @click="() => (collapsed = !collapsed)" />
            </a-layout-header>
            <a-layout-content :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }">
                <router-view />
            </a-layout-content>
        </a-layout>
    </a-layout>
</template>

<script setup>
import store from "@/store";
import { computed, ref, watch } from 'vue';
import Cookie from 'js-cookie';
import { useRouter } from "vue-router"
import { MenuUnfoldOutlined, MenuFoldOutlined, UnorderedListOutlined, UserOutlined } from '@ant-design/icons-vue';
const pathChange = computed(() => {
    return store.state.newPath;
})

watch(pathChange, (newVal, oldVal) => {

}, { immediate: true, deep: true })
const selectedKeys = ref([useRouter().currentRoute._rawValue.path]);
const collapsed = ref(false);
var title = ref(Cookie.get("student_name"));
</script>

<style>
#components-layout-demo-custom-trigger {
    height: 100vh;
}

#components-layout-demo-custom-trigger .trigger {
    font-size: 18px;
    line-height: 64px;
    padding: 0 24px;
    cursor: pointer;
    transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
    color: #1890ff;
}

#components-layout-demo-custom-trigger .logo {
    height: 32px;
    background: rgba(255, 255, 255, 0.3);
    margin: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
}

.site-layout .site-layout-background {
    background: #fff;
}
</style>