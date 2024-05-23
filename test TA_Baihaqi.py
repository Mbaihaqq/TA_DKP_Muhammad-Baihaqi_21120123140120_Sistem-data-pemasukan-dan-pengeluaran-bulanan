import tkinter as tk

class SistemDataBulanan:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Data Pendapatan dan Pengeluaran Bulanan")
        self.root.geometry("400x450")

        self.kategori_pengeluaran = ["Sewa", "Utilitas", "Makanan", "Transportasi", "Hiburan", "Lainnya"]

        self.pendapatan_label = tk.Label(root, text="Pendapatan Bulanan:")
        self.pendapatan_label.pack()
        self.pendapatan_entry = tk.Entry(root)
        self.pendapatan_entry.pack()

        self.pengeluaran_label = tk.Label(root, text="Pengeluaran:")
        self.pengeluaran_label.pack()
        self.pengeluaran_frame = tk.Frame(root)
        self.pengeluaran_frame.pack()

        self.entries = []
        for i, kategori in enumerate(self.kategori_pengeluaran):
            tk.Label(self.pengeluaran_frame, text=kategori).grid(row=i, column=0)
            entry = tk.Entry(self.pengeluaran_frame, width=10)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        self.hitung_button = tk.Button(root, text="Hitung", command=self.hitung)
        self.hitung_button.pack()

        self.hasil_label = tk.Label(root, text="")
        self.hasil_label.pack()

        self.data_pengeluaran_label = tk.Label(root, text="Data Pengeluaran:")
        self.data_pengeluaran_label.pack()
        self.data_pengeluaran_text = tk.Text(root, height=10, width=40)
        self.data_pengeluaran_text.pack()

    def hitung(self):
        self.hasil_label.config(text="", fg="black")
        self.data_pengeluaran_text.delete(1.0, tk.END)

        try:
            pendapatan = int(self.pendapatan_entry.get())
        except ValueError:
            self.hasil_label.config(text="Pendapatan harus diisi dengan angka!", fg="red")
            return

        total_pengeluaran = 0
        pengeluaran_list = []

        for i, entry in enumerate(self.entries):
            try:
                jumlah = int(entry.get())
                if jumlah < 0:
                    self.hasil_label.config(text="Pengeluaran tidak boleh kurang dari 0!", fg="red")
                    return
                pengeluaran_list.append((self.kategori_pengeluaran[i], jumlah))
                total_pengeluaran += jumlah
            except ValueError:
                entry.delete(0, tk.END)
                entry.insert(0, "0")

        if total_pengeluaran > pendapatan:
            self.hasil_label.config(text="Total pengeluaran tidak boleh lebih besar dari pendapatan!", fg="red")
            return

        saldo_tersisa = pendapatan - total_pengeluaran

        self.data_pengeluaran_text.insert(tk.END, f"Pendapatan Bulanan: {pendapatan}\n")
        self.data_pengeluaran_text.insert(tk.END, f"Total Pengeluaran: {total_pengeluaran}\n")
        self.data_pengeluaran_text.insert(tk.END, f"Saldo Tersisa: {saldo_tersisa}\n\n")
        self.data_pengeluaran_text.insert(tk.END, "Rincian Pengeluaran:\n")
        for kategori, jumlah in pengeluaran_list:
            self.data_pengeluaran_text.insert(tk.END, f"{kategori}: {jumlah}\n")

        self.hasil_label.config(text="Perhitungan berhasil.", fg="green")

def main():
    root = tk.Tk()
    app = SistemDataBulanan(root)
    root.mainloop()

if __name__ == "__main__":
    main()