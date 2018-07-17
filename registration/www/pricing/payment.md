# Pilihan Cara Pembayaran

<!-- jinja -->
<table class="table table-bordered table-hover">
	<thead>
		<tr>
			<th style="width: 20%;">Paket</th>
			<th class="text-center">Bank BCA</th>
			<th class="text-center">Bank BRI</th>
			<th class="text-center">Indomaret</th>
			<th class="text-center">Doku Wallet</th>
			<th class="text-center">Counter</th>
		</tr>
	</thead>
	<tbody>
		{% for plan in [
			{"name": "Wulan", "idr": "150,000", "idr": "150,000", "usd": "150,000"},
			{"name": "Tria", "idr": "425,000", "idr": "425,000", "usd": "150,000"},
			{"name": "Seta", "idr": "800,000", "idr": "800,000", "usd": "150,000"},
			{"name": "Warsa", "idr": "1,500,000", "idr": "1,500,000", "usd": "150,000"},
			] -%}
		{% set idr = frappe.utils.fmt_money(plan.idr, precision=0, currency="IDR") %}

			<tr>
				<td>{{ plan.name }}</td>
				<td class="text-center"><a class="bca-wire-transfer" data-amount="{{ idr }}" onclick="pay.wire_transfer(this, '.bca-wire-transfer-msg')">{{ idr }}</a></td>
				<td class="text-center"><a class="bri-wire-transfer" data-amount="{{ idr }}" onclick="pay.wire_transfer(this, '.bri-wire-transfer-msg')">{{ idr }}</a></td>
				<td class="text-center"><a class="indomaret-wire-transfer" data-amount="{{ idr }}" onclick="pay.wire_transfer(this, '.indomaret-wire-transfer-msg')">{{ idr }}</a></td>
				<td class="text-center"><a class="dokuwallet-wire-transfer" data-amount="{{ idr }}" onclick="pay.wire_transfer(this, '.dokuwallet-wire-transfer-msg')">{{ idr }}</a></td>
				<td class="text-center"><a class="mall-wire-transfer" data-amount="{{ idr }}" onclick="pay.wire_transfer(this, '.mall-wire-transfer-msg')">{{ idr }}</a></td>
			</tr>
		{%- endfor %}
	</tbody>
</table>

<!-- popup messages bca-->
<div class="bca-wire-transfer-msg hidden">
<p class="text-muted">Jumlah ini sudah termasuk PPN 10%</p>
<hr>

	<h4>Cara 1: Transfer melalui ATM</h4>
	<p>Anda dapat mentransfer jumlah pembayaran langsung melalui ATM atau mobile banking BCA ke rekening kami.</p>
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td width="30%">Nama Bank</td>
				<td>Bank BCA</td>
			</tr>
			<tr>
				<td>Alamat Bank</td>
				<td>Jl. XXX, Jakarta, Indonesia.</td>
			</tr>
			<tr>
				<td>Nomor Rekening</td>
				<td>0123456789</td>
			</tr>
			<tr>
				<td>Nama Rekening</td>
				<td>PT. Integria Nusa Cendekia</td>
			</tr>
		</tbody>
	</table>

	<hr>
	<h4>Cara 2: Setor ke Bank</h4>
	<p>Anda juga dapat melakukan pembayaran melalui setoran langsung ke kasir di kantor cabang bank BCA</p>
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td>Nomor Rekening</td>
				<td>0123456789</td>
			</tr>
			<tr>
				<td>Nama Rekening</td>
				<td>PT. Integria Nusa Cendekia</td>
			</tr>
		</tbody>
	</table>
	<hr>
	<h4>Catatan:</h4>
	<ul>
		<li>Biaya transfer dan biaya bank lainnya ditanggung oleh anda.</li>
		<li>Harap segera konfirmasikan pembayaran anda kepada kami supaya kami dapat segera memperbarui data anda.</li>
	</ul>
</div>


<!-- popup messages bri-->
<div class="bri-wire-transfer-msg hidden">
<p class="text-muted">Jumlah ini sudah termasuk PPN 10%</p>
<hr>

	<h4>Cara 1: Transfer melalui ATM</h4>
	<p class="text-muted">Anda dapat mentransfer jumlah pembayaran langsung melalui ATM atau mobile banking BRI ke rekening kami.</p>
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td width="30%">Nama Bank</td>
				<td>Bank BRI</td>
			</tr>
			<tr>
				<td>Alamat Bank</td>
				<td>Jl. XXX, Jakarta, Indonesia.</td>
			</tr>
			<tr>
				<td>Nomor Rekening</td>
				<td>0123456789</td>
			</tr>
			<tr>
				<td>Nama Rekening</td>
				<td>PT. Integria Nusa Cendekia</td>
			</tr>
		</tbody>
	</table>

	<hr>
	<h4>Cara 2: Setor ke Bank</h4>
	<p class="text-muted">Anda juga dapat melakukan pembayaran melalui setoran langsung ke kasir di kantor cabang bank BRI</p>
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td>Nomor Rekening</td>
				<td>0123456789</td>
			</tr>
			<tr>
				<td>Nama Rekening</td>
				<td>PT. Integria Nusa Cendekia</td>
			</tr>
		</tbody>
	</table>
	<hr>
	<h4>Catatan:</h4>
	<ul>
		<li>Biaya transfer dan biaya bank lainnya ditanggung oleh anda.</li>
		<li>Harap segera konfirmasikan pembayaran anda kepada kami supaya kami dapat segera memperbarui data anda.</li>
	</ul>
</div>


<!-- popup messages indomaret-->
<div class="indomaret-wire-transfer-msg hidden">
<p class="text-muted">Jumlah ini sudah termasuk PPN 10%</p>
<hr>
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td width="30%">Nama Toko</td>
				<td>Indomaret</td>
			</tr>
			<tr>
				<td>Alamat</td>
				<td>Jl. xxx, Jakarta, Indonesia:</td>
			</tr>
			<tr>
				<td>Cabang</td>
				<td>Semua Cabang</td>
			</tr>
			<tr>
				<td>No. Rekening</td>
				<td>1234567890</td>
			</tr>
			<tr>
				<td>Nama Rekening</td>
				<td>PT. Integria Nusa Cendekia</td>
			</tr>
		</tbody>
	</table>
	<hr>
	<h4>Catatan:</h4>
	<ul>
		<li>Biaya pembayaran yang dikenakan oleh Indomaret menjadi tanggungan anda.</li>
		<li>Harap segera konfirmasikan pembayaran anda kepada kami supaya kami dapat segera memperbarui data anda.</li>
	</ul>
</div>


<!-- popup messages doku wallet-->
<div class="dokuwallet-wire-transfer-msg hidden">
<p class="text-muted">Jumlah ini sudah termasuk PPN 10%</p>
<hr>
	<table class="table table-bordered table-hover">
		<tbody>
			<tr>
				<td width="30%">Nama App</td>
				<td>Doku Wallet</td>
			</tr>
			<tr>
				<td>Alamat</td>
				<td>Jl. xxx, Jakarta, Indonesia:</td>
			</tr>
			<tr>
				<td>Cabang</td>
				<td>Semua Cabang</td>
			</tr>
			<tr>
				<td>No. Rekening</td>
				<td>1234567890</td>
			</tr>
			<tr>
				<td>Nama Rekening</td>
				<td>PT. Integria Nusa Cendekia</td>
			</tr>
		</tbody>
	</table>
	<hr>
	<h4>Catatan:</h4>
	<ul>
		<li>Biaya transfer dan biaya lainnya, jika ada, ditanggung oleh anda.</li>
		<li>Harap segera konfirmasikan pembayaran anda kepada kami supaya kami dapat segera memperbarui data anda.</li>
	</ul>
</div>


<!-- popup mall -->
<div class="mall-wire-transfer-msg hidden">
<p class="text-muted">Jumlah ini sudah termasuk PPN 10%</p>
<hr>
<h4>Melalui Counter Punia</h4>
<p>Anda dapat membayar pada counter-counter Punia yang tersedia di berbagai lokasi di kota anda.</p>
<p>Untuk membayar melalui counter, silahkan menyiapkan beberapa informasi:</p>
<p>
	<ul>
		<li>Nama Usaha</li>
		<li>Nama Pemilik Usaha</li>
		<li>Nomor Anggota</li>
	</ul>
</p>
<hr>
<p>Beberapa lokasi yang terdapat counter Punia:</p>
	<table class="table table-bordered table-hover">
		<thead>
			<tr>
				<th style="width: 30%;">Nama Tempat</th>
				<th class="text-center">Alamat</th>
				<th class="text-center">Lokasi</th>
			</tr>
		</thead>
		<tbody>
			<tr><td>Mall A</td><td>Jl. xxx, Jakarta, Indonesia:</td><td>Lantai Dasar</td></tr>
			<tr><td>Mall B</td><td>Jl. xxx, Jakarta, Indonesia:</td><td>Lantai Dasar</td></tr>
			<tr><td>Mall C</td><td>Jl. xxx, Jakarta, Indonesia:</td><td>Lantai Dasar</td></tr>
			<tr><td>Mall D</td><td>Jl. xxx, Jakarta, Indonesia:</td><td>Lantai Dasar</td></tr>
			<tr><td>Mall E</td><td>Jl. xxx, Jakarta, Indonesia:</td><td>Lantai Dasar</td></tr>
			<tr><td>Mall F</td><td>Jl. xxx, Jakarta, Indonesia:</td><td>Lantai Dasar</td></tr>
		</tbody>
	</table>
	<hr>
	<h4>Catatan:</h4>
	<ul>
		<li>Simpanlah tanda bukti pembayaran anda.</li>
	</ul>
</div>
