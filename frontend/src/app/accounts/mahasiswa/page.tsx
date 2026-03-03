"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  GraduationCap,
  FileText,
  CheckCircle,
  LayoutDashboard,
  File,
  PanelLeftClose,
  PanelLeftOpen,
  ChevronDown,
  ChevronRight,
  Upload,
  Download,
  Archive,
} from "lucide-react"
import Link from "next/link"


export default function MahasiswaPage() {
  const [user] = useState({
    name: "Coba Mahasiswa",
    email: "mahasiswa@example.com",
  })
  const [isSidebarOpen, setIsSidebarOpen] = useState(true)
  const [isDocsOpen, setIsDocsOpen] = useState(true)

  return (
    <div className="min-h-screen flex bg-muted/40 relative">
      {/* Sidebar */}
      <aside
        className={`bg-background border-r p-6 flex flex-col justify-between transition-all duration-300 ${
          isSidebarOpen ? "w-64 translate-x-0" : "w-0 -translate-x-full p-0 border-r-0"
        } absolute md:static h-full md:h-auto z-40 overflow-hidden`}
      >
        <div className="space-y-6">
          <h2 className="text-xl font-bold">Portal Mahasiswa</h2>

          <nav className="space-y-2">
            <Button variant="ghost" className="w-full justify-start gap-2">
              <LayoutDashboard className="h-4 w-4" /> Dashboard
            </Button>
            
            {/* Dropdown Menu untuk Dokumen */}
            <Collapsible
              open={isDocsOpen}
              onOpenChange={setIsDocsOpen}
              className="w-full"
            >
              <CollapsibleTrigger asChild>
                <Button variant="ghost" className="w-full justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <File className="h-4 w-4" />
                    <span>Dokumen</span>
                  </div>
                  {isDocsOpen ? (
                    <ChevronDown className="h-4 w-4" />
                  ) : (
                    <ChevronRight className="h-4 w-4" />
                  )}
                </Button>
              </CollapsibleTrigger>
              <CollapsibleContent className="pl-6 space-y-1 mt-1">
                <Button variant="ghost" className="w-full justify-start gap-2 text-sm">
                  <FileText className="h-3 w-3" /> Semua Dokumen
                </Button>
                <Button variant="ghost" className="w-full justify-start gap-2 text-sm">
                  <Upload className="h-3 w-3" /> Upload Dokumen
                </Button>
                <Button variant="ghost" className="w-full justify-start gap-2 text-sm">
                  <Download className="h-3 w-3" /> Download Template
                </Button>
                <Button variant="ghost" className="w-full justify-start gap-2 text-sm">
                  <Archive className="h-3 w-3" /> Arsip
                </Button>
              </CollapsibleContent>
            </Collapsible>
          </nav>
        </div>

        <p className="text-xs text-muted-foreground">
          © 2026 Sistem Pendaftaran
        </p>
      </aside>


      <div className="flex-1 flex flex-col">
        <header className="h-16 border-b bg-background flex items-center justify-between px-6">
          <div className="flex items-center gap-2">
            <Button
              variant="ghost"
              size="icon"
              onClick={() => setIsSidebarOpen((prev) => !prev)}
              aria-label={isSidebarOpen ? "Hide sidebar" : "Show sidebar"}
            >
              {isSidebarOpen ? (
                <PanelLeftClose className="h-5 w-5" />
              ) : (
                <PanelLeftOpen className="h-5 w-5" />
              )}
            </Button>
            <h1 className="text-lg font-semibold">Dashboard</h1>
          </div>

          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" className="flex items-center gap-3">
                <Avatar className="h-8 w-8">
                  <AvatarFallback>
                    {user.name
                      .split(" ")
                      .map((n) => n[0])
                      .join("")}
                  </AvatarFallback>
                </Avatar>
                <span className="hidden sm:inline text-sm font-medium">
                  {user.name}
                </span>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-40">
              <DropdownMenuItem>Account</DropdownMenuItem>
              <Link href="/">
                <DropdownMenuItem className="text-red-500">
                    Logout
                </DropdownMenuItem>
              </Link>
            </DropdownMenuContent>
          </DropdownMenu>
        </header>

        <main className="p-6 space-y-8">
          <div>
            <h2 className="text-3xl font-bold tracking-tight">
              Dashboard Mahasiswa
            </h2>
            <p className="text-muted-foreground">
              Ringkasan informasi pendaftaran dan status akun Anda
            </p>
          </div>


          <div className="grid gap-6 md:grid-cols-3">
            <Card className="rounded-2xl shadow-sm">
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium text-muted-foreground">
                  Status Pendaftaran
                </CardTitle>
                <FileText className="h-5 w-5 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-lg font-semibold">
                  Sedang Diverifikasi
                </div>
              </CardContent>
            </Card>

            <Card className="rounded-2xl shadow-sm">
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium text-muted-foreground">
                  Kelengkapan Berkas
                </CardTitle>
                <GraduationCap className="h-5 w-5 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  <Progress value={75} />
                  <p className="text-sm text-muted-foreground">
                    75% lengkap
                  </p>
                </div>
              </CardContent>
            </Card>

            <Card className="rounded-2xl shadow-sm">
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium text-muted-foreground">
                  Hasil Seleksi
                </CardTitle>
                <CheckCircle className="h-5 w-5 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-lg font-semibold">
                  Belum Tersedia
                </div>
              </CardContent>
            </Card>
          </div>

          <Card className="rounded-2xl shadow-sm">
            <CardHeader>
              <CardTitle>Riwayat Upload Dokumen</CardTitle>
              <CardDescription>
                Daftar dokumen yang telah Anda unggah
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Nama Dokumen</TableHead>
                    <TableHead>Status</TableHead>
                    <TableHead>Tanggal Upload</TableHead>
                    <TableHead className="text-right">Aksi</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  <TableRow>
                    <TableCell>Kartu Identitas</TableCell>
                    <TableCell>Valid</TableCell>
                    <TableCell>12 Jan 2026</TableCell>
                    <TableCell className="text-right">
                      <Button size="sm" variant="outline">
                        Lihat
                      </Button>
                    </TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>Ijazah</TableCell>
                    <TableCell>Menunggu Verifikasi</TableCell>
                    <TableCell>14 Jan 2026</TableCell>
                    <TableCell className="text-right">
                      <Button size="sm" variant="outline">
                        Lihat
                      </Button>
                    </TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </CardContent>
          </Card>
        </main>
      </div>
    </div>
  )
}