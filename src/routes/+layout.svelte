<script lang="ts">
  import "../app.css";
  import { House, Building2, Users, Trophy, Megaphone, Info } from '@lucide/svelte';
  import * as Card from "$lib/components/ui/card/index.js";
  import BottomNav from "$lib/components/BottomNav.svelte";
  import Navbar from "$lib/components/Navbar.svelte";
  import logo from "$lib/assets/extended-logo-sn-black.png";
  import { resolve } from "$app/paths";

  const navItems = [
    { label: "Inicio", shortLabel: "Inicio", icon: House, href: resolve("/")},
    { label: "USM", shortLabel: "USM", icon: Building2, href: resolve("/usm") },
    { label: "Iniciativas", shortLabel: "Iniciativas", icon: Users, href: resolve("/iniciativas") },
    { label: "Deportes", shortLabel: "Deportes", icon: Trophy, href: resolve("/deportes") },
    { label: "Centros Estudiantiles", shortLabel: "Centros", icon: Megaphone, href: resolve("/centros") },
    { label: "Sobre Nosotros", shortLabel: "Nosotros", icon: Info, href: resolve("/nosotros") },
  ];

  let { children } = $props();
</script>


<div class="grid grid-cols-12">
  <header class="col-span-12 md:col-span-8 md:col-start-3">
    <div class=" md:px-4 md:py-8">

      <!-- Logo -->
      <div class="mb-6">
        <a href={resolve("/")}>
          <img src={logo} class="mx-auto w-full max-w-lg" alt="SansaNews Logo"/>
        </a>
      </div>

      <Navbar {navItems} />
      <BottomNav {navItems} />
    </div>
  </header>

  <!-- Banner -->
  <div class="col-span-12 px-4 md:col-span-8 md:col-start-3">
    <Card.Root class="gap-0 border-0 py-0">
      <Card.Header class="bg-foreground text-background rounded-t-lg py-2">
        <Card.Title
          class="text-center text-sm font-bold tracking-widest uppercase"
        >
          <p>alpha-1.1.0</p>
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
