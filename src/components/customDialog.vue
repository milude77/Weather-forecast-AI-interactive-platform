<template>
    <el-dialog v-model="visible" :title="title" :width="width">
      <span>{{ message }}</span>
      <template #footer>
        <el-button @click="closeDialog">{{ this.cancelButtonText }}</el-button>
        <el-button type="primary" @click="handleConfirm">{{this.confirmButtonText}}</el-button>
      </template>
    </el-dialog>
</template>
  
<script>

export default {
    name: "customDialog",
    props: {
        modelValue: {
            type: Boolean,
            required: true
        },
        title: {
            type: String,
            default: "提示"
        },
        message: {
            type: String,
            required: true
        },
        width: {
            type: String,
            default: "30%"
        },
        confirmButtonText: {
            type: String,
            default: "确定"
        },
        cancelButtonText: {
            type: String,
            default: "取消"
        },
        confirmAction: {
            type: Function,
            default: () => {}
        },
        cancelAction: {
            type: Function,
            default: () => {}
        }
    },
    computed: {
        visible: {
            get() {
                return this.modelValue;
            },
            set(value) {
                this.$emit('update:modelValue', value);
            }
        }
    },
    methods: {
        closeDialog() {
            this.cancelAction();
            this.$emit('cancel');
            this.visible = false;
        },
        confirmDialog() {
            this.$emit('confirm');
            this.visible = false;
        },
        handleConfirm() {
            this.confirmAction();
            this.confirmDialog();
        }
    }
};
</script>