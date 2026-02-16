<script lang="ts">
  import "../app.css";
  import * as Card from "$lib/components/ui/card/index.js";
  import MobileMenu from "$lib/components/MobileMenu.svelte";
  import Navbar from "$lib/components/Navbar.svelte";
  import logo from "$lib/assets/extended-logo-sn-black.png";
  import { resolve } from "$app/paths";

  const navItems = [
    { label: "Inicio", href: resolve("/") },
    { label: "USM", href: resolve("/usm") },
    { label: "Iniciativas", href: resolve("/iniciativas") },
    { label: "Deportes", href: resolve("/deportes") },
    { label: "Centros Estudiantiles", href: resolve("/centros") },
    { label: "Sobre Nosotros", href: resolve("/nosotros") },
  ];

  let { children } = $props();
</script>

<svelte:head>
  <meta charset="UTF-8" />
  <title>SansaNews</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="SansaNews es un medio de comunicación automatizado que visibiliza las iniciativas estudiantiles de la USM" />

  <!-- Iconos -->
  <link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="shortcut icon" href="/favicon.ico" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <meta name="apple-mobile-web-app-title" content="SansaNews" />
  <meta name="theme-color" content="#03989E" />
  <link rel="manifest" href="/sansanews.webmanifest" />
</svelte:head>

<div class="grid grid-cols-12">
  <header class="col-span-12 md:col-span-8 md:col-start-3">
    <div class="px-4 py-8">

      <!-- Logo -->
      <div class="mb-6">
        <a href={resolve("/")}>
          <img src={logo} class="mx-auto w-full max-w-lg" alt="SansaNews Logo"/>
        </a>
      </div>

      <Navbar {navItems} />
      <MobileMenu {navItems} />
    </div>
  </header>

  <!-- Banner -->
  <div class="col-span-12 px-4 md:col-span-8 md:col-start-3">
    <Card.Root class="gap-0 border-0 py-0">
      <Card.Header class="bg-foreground text-background rounded-t-lg py-2">
        <Card.Title
          class="text-center text-sm font-bold tracking-widest uppercase"
        >
          <p>alpha-1.0.3</p>
        </Card.Title>
      </Card.Header>
      <Card.Content class="p-4 text-center">
        <h2 class="mb-2 font-[--font-heading] text-xl font-bold md:text-2xl">
          WORK IN PROGRESS
        </h2>
        <p class="text-muted-foreground text-xs tracking-wide sm:text-sm">
          SansaNews se encuentra en la fase inicial de desarrollo, pronto se
          implementaran secciones nuevas y mejoras en la interfaz.
        </p>
        <p class="text-muted-foreground text-xs tracking-wide sm:text-sm">
          ¡Gracias por ser parte de este proceso!
        </p>
      </Card.Content>
    </Card.Root>
  </div>

  <div class="col-span-12 md:col-span-8 md:col-start-3">
    {@render children()}
  </div>

  <footer
    class="text-muted-foreground col-span-12 border-t-3 border-double p-6 text-center text-sm font-medium"
  >
    <p class="px-4">
      SansaNews es un medio de comunicación automatizado que visibiliza las
      iniciativas estudiantiles de la USM
    </p>
  </footer>
</div>
