<script lang="ts">
  import { data } from '../stores';
  import { scaleLinear } from 'd3-scale';
  import { range } from 'd3-array';

  export let width: number;
  export let height: number;

  const margin = { top: 20, right: 20, bottom: 40, left: 40 };
  const radius = 3;
  const tickSize = 6;

  $: x = scaleLinear()
    .domain([Math.min(...$data.x), Math.max(...$data.x)])
    .nice()
    .range([margin.left, width - margin.right]);

  $: y = scaleLinear()
    .domain([Math.min(...$data.y), Math.max(...$data.y)])
    .nice()
    .range([height - margin.bottom, margin.top]);

  $: I = range($data.x.length);
</script>

<svg {width} {height}>
  <!-- dots -->
  <g>
    {#each I as i}
      <circle
        r={radius}
        cx={x($data.x[i])}
        cy={y($data.y[i])}
        fill="steelblue"
      />
    {/each}
  </g>

  <!-- x axis -->
  <g transform="translate(0,{height - margin.bottom})">
    {#each x.ticks() as tick}
      <g transform="translate({x(tick)})">
        <line y1={0} y2={tickSize} stroke="black" />
        <text
          y={tickSize + 2}
          text-anchor="middle"
          dominant-baseline="hanging"
          font-size="12"
        >
          {tick}
        </text>
      </g>
    {/each}
  </g>

  <!-- y axis -->
  <g transform="translate({margin.left})">
    {#each y.ticks() as tick}
      <g transform="translate(0,{y(tick)})">
        <line x1={0} x2={-tickSize} stroke="black" />
        <text
          x={-tickSize - 2}
          text-anchor="end"
          dominant-baseline="middle"
          font-size="12"
        >
          {tick}
        </text>
      </g>
    {/each}
  </g>
</svg>

<style>
</style>
