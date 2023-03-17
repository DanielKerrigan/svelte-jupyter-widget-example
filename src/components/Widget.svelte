<script lang="ts">
  import ScatterPlot from './ScatterPlot.svelte';
  import { height } from '../stores';
</script>

<div class="svelte-widget-container" style:height="{$height}px">
  <ScatterPlot width={$height} height={$height} />
</div>

<style>
  .svelte-widget-container {
    box-sizing: border-box;
    width: 100%;
    font-size: 16px;
    border: 1px solid #eeeeee;
    background-color: white;
    color: black;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
